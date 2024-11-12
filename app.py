from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

with open('api_database.json', 'r') as f:
    api_database = json.load(f)
    
with open('customer_preferences.json', 'r') as f:
    customer_preferences_data = json.load(f)
    
with open('templates/standard.txt', 'r') as f:
    standard_template = f.read()
    
app = Flask(__name__)

def get_customer_preferences(customer_name):
    for customer in customer_preferences_data:
        if customer.get("customer_name") == customer_name:
            return customer
    return {}

def run_llm(prompt):
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
    #fetched_APIs = content.split('Fetched APIs:')[1].split('HTML Code:')[0]
    HTML_code = content.split("```html")[1].split("```")[0]
    print(HTML_code)
    return HTML_code


def create_website(customer, user_input):
    customer_preferences = get_customer_preferences(customer)
    prompt = f'''
    Customer Preferences = {customer_preferences}
    Fetch relevant APIs for the UI elements mentioned in {user_input} 
    from the existing database of UI elements in {api_database} and convert them into HTML code, including style specifications in the customer preferences.
    Modify the following html template with the generated HTML code:
    {standard_template} 
    Answer only in modified HTML code. 
    ...'''
    html = run_llm(prompt)
    return html
    
@app.route('/', methods = ['GET', 'POST'])
def index():
    generated_HTML = None
    if request.method == 'POST':
        customer = request.form['user']
        user_prompt = request.form['instructions']
        generated_HTML = create_website(customer, user_prompt)
    return render_template('index.html', generated_html=generated_HTML)
        
if __name__ == '__main__':
    app.run(debug=True)