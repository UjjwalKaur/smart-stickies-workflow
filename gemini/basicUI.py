'''
Created on Oct 11, 2024

@author: Pranav
'''

import os
import google.generativeai as genai


GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

sample_pdf = genai.upload_file("api_database.pdf")
#summary = model.generate_content(["Give me a summary of this pdf file.", sample_pdf])
#print(summary)

user_input = input("What UI would you like to create today? ")

# Split user input into different UI elements
ui_elements = user_input.split(" and ")
print(ui_elements)

# Get the API for each element the user wants
for i, val in enumerate(ui_elements):
    prompt = "Get the UI element(s) for " + val + " from this pdf file. Give me only the endpoint and payload."
    response = model.generate_content([prompt, sample_pdf])
    print("Element " + str(i) + "\n" + response.text)
    
    # Construct an HTTP POST request with the retrieved JSON