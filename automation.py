# this is the task C 

import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import os

#this will search the image in the google and save ir
def search_image_on_google(query):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/imghp?hl=en")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    pyautogui.rightClick(500, 600)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(3)
    pyautogui.press('enter')    
    time.sleep(3)
    pyautogui.press('enter')
    driver.quit()

# this is saving the text through wikepedia     
def search_text_on_google(topic) :
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(topic)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    time.sleep(3)    
    driver.quit()

#this is copying the text of the wekipedia
def save_in_word(topic) :
    pyautogui.press('win')
    time.sleep(3)
    pyautogui.write('word')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl','n')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl','v')
    time.sleep(4)        
    pyautogui.hotkey('ctrl','s')
    time.sleep(3)
    pyautogui.press('enter')

# this is the modal 
st.title('Search Topic data on Google')
st.write("This bot will give you the image and the wekipedia data of the topic")
topic = st.text_input("Enter the topic:")
if st.button('Search Data'):
    if topic:
        search_image_on_google(topic)
        st.success('search is done and image is saved')
        
        search_text_on_google(topic)
        st.success('Text is copid')

        save_in_word(topic)
        st.success('Word document is ready')
        time.sleep(3)
        
    else:
        st.error('Please enter a topic to search for an image.')
