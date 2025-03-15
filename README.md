```markdown
# Project Name: Text Bots with Automation

## Description
Explore different bots that help you generate text in various ways. This project integrates image-to-text recognition, audio-to-text conversion, and text generation, all powered by state-of-the-art models. It also features an automation page where users can generate content and convert media files.

## Python Libraries
1. **ReactPy**: Used for creating the UI of the welcome page.
2. **Gradio**: Used for displaying the models and interacting with them.
3. **Transformers**: Used for encoding and decoding image, audio, and text.

## Pretrained Models
1. **Tesseract OCR**: Used for converting images to text (Image-to-Text Recognition).
2. **Speech Recognition**: Converts audio to text.
3. **GPT-2**: Generates text based on the input text.
4. **Sentiment Analyzer**: Performs sentiment analysis on text.

*Note: These models were referenced from existing sources.*

## How to Run the Project

### Step 1: Setup the Virtual Environment

1. **Create a virtual environment** in PowerShell:
   ```bash
   python -m venv env
   ```

2. **Activate the virtual environment**:
   ```bash
   cd env\Scripts
   .\activate
   ```

3. **Install required libraries** inside the virtual environment:
   Make sure you're inside the activated `venv`:
   ```bash
   pip install reactpy transformers gradio pytesseract SpeechRecognition streamlit
   ```

### Step 2: Run the Project

1. Open **three terminals** simultaneously.

2. In the first terminal, run the **UI**:
   ```bash
   python ui.py
   ```
   This will run the main home page of the project on the local server.

3. In the second terminal, run the **Gradio bots**:
   ```bash
   python app.py
   ```
   This will activate the Gradio bots on a local server.

4. In the third terminal, run the **Automation page**:
   ```bash
   streamlit automation.py
   ```
   This will activate the automation page on a local server.

## Folder Structure
```plaintext
Project
│
├── env               # Virtual environment
├── ui.py             # Main home page UI (ReactPy)
├── app.py            # Gradio bot integration
├── automation.py     # Automation logic (Streamlit)
```

## Screenshots of the Pages

### 1. Home Page
![Home Page Screenshot](link_to_homepage_image.png)

### 2. Bots Page
#### 1. Image Analyzer
![Image Analyzer Screenshot](link_to_image_analyzer_image.png)

#### 2. Audio Analyzer
![Audio Analyzer Screenshot](link_to_audio_analyzer_image.png)

#### 3. Text Analyzer
![Text Analyzer Screenshot](link_to_text_analyzer_image.png)

### 3. Automation Page
![Automation Page Screenshot](link_to_automation_page_image.png)

---

*Feel free to explore the bots and automation features, and don’t hesitate to reach out for any questions or suggestions!*

```

### Explanation:
- **Step 1** covers creating and activating a virtual environment.
- **Step 2** runs the three main components of the project (`ui.py`, `app.py`, and `automation.py`), each in its own terminal.
- **Folder structure** explains the organization of the project files.
- **Screenshots** sections give placeholders for adding images of each page in the project. You can replace the placeholder links (`link_to_homepage_image.png`, etc.) with actual image URLs for the project screenshots.
