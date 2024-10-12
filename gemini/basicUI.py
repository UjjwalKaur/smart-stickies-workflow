'''
Created on Oct 11, 2024

@author: Pranav
'''

import os
import webbrowser
import google.generativeai as genai

GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = input("What UI would you like to create today? ")
response = model.generate_content(user_input + " Start your response with \"<!DOCTYPE html>\" and end with \"< html>\"")

html_content = response.text
with open('temp.html', 'w') as f:
    f.write(html_content)
webbrowser.open_new_tab('temp.html')