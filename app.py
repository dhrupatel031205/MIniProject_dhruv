# this is the task B

import gradio as gr
import pytesseract
from PIL import Image
import speech_recognition as sr
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if needed

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

sentiment_analyzer = pipeline("sentiment-analysis")

def image_to_text(image):
    if image is not None:
        text = pytesseract.image_to_string(image)
        return text if text.strip() else "No text detected in the image."
    return "No image uploaded."

def audio_to_text(audio):
    recognizer = sr.Recognizer()
    if audio is not None:
        # Ensure the file path is correctly handled
        with sr.AudioFile(audio) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                return text if text.strip() else "No speech detected."
            except sr.UnknownValueError:
                return "Speech Recognition could not understand audio."
            except sr.RequestError as e:
                return f"Could not request results; {e}"
    return "No audio uploaded."

def text_to_text(text):
    if text:
        # Tokenize the input text
        inputs = tokenizer.encode(text, return_tensors="pt")
        # Generate text with GPT-2
        outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Perform sentiment analysis line by line
        lines = text.split("\n")
        sentiment_results = []
        for line in lines:
            if line.strip():  # Avoid empty lines
                sentiment = sentiment_analyzer(line)[0]
                sentiment_results.append(f"Line: {line}\nSentiment: {sentiment['label']} (confidence: {sentiment['score']:.2f})")
        
        # Combine the results: the generated text and the sentiment analysis results
        sentiment_output = "\n\n".join(sentiment_results)
        return generated_text, sentiment_output
    return "No text provided."


with gr.Blocks() as demo:
    gr.Markdown("## Text Conversion ")

    with gr.Tab("Image Analyzer"):
        gr.Markdown("Upload an image to extract text:")
        img_input = gr.Image(type="pil", label="Upload Image", elem_id="img_input")
        img_output = gr.Textbox(label="Extracted Text", elem_id="img_output")
        img_button = gr.Button("Convert", elem_id="img_button")
        img_button.click(fn=image_to_text, inputs=img_input, outputs=img_output)

    with gr.Tab("Audio Analyser"):
        gr.Markdown("Upload an audio file to convert speech to text:")
        audio_input = gr.Audio(type="filepath", label="Upload Audio", elem_id="audio_input")
        audio_output = gr.Textbox(label="Recognized Text", elem_id="audio_output")
        audio_button = gr.Button("Convert", elem_id="audio_button")
        audio_button.click(fn=audio_to_text, inputs=audio_input, outputs=audio_output)

    with gr.Tab("Text Analyser"):
        gr.Markdown("Enter some text to generate a description and analyze sentiment:")
        text_input = gr.Textbox(label="Input Text", lines=5, elem_id="text_input")
        text_output = gr.Textbox(label="Generated Description", elem_id="text_output")
        sentiment_output = gr.Textbox(label="Sentiment Analysis", elem_id="sentiment_output")
        text_button = gr.Button("Generate Description and Sentiment", elem_id="text_button")
        text_button.click(fn=text_to_text, inputs=text_input, outputs=[text_output, sentiment_output])

demo.launch()
