from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

with open('api_database.json', 'r') as f:
    api_database = json.load(f)

user_input = "Make a website with two buttons and a slider"
prompt = f'''
Fetch relevant APIs for the UI elements mentioned in {user_input} 
from the exisiting database of UI elements in {api_database}. 
After fetching the UIs, write HTML code for the website using the specifications in the fetched API.
Response Structure:
Fetched APIs:
...
HTML Code
...'''

client = Groq()
completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=1,
    max_tokens=2024,
    top_p=1,
    stream=True,
    stop=None,
)
content = ''
for chunk in completion:
    content = content + (chunk.choices[0].delta.content or "")
    
fetched_APIs = content.split('Fetched APIs:')[1].split('HTML Code:')[0]
HTML_code = content.split("```html")[1].split("```")[0]

with open('fetch_api.txt', 'w') as f:
    f.write(f'APIs \n{fetched_APIs}')
    
with open('sample.html', 'w') as f:
    f.write(HTML_code)