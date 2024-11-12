# SmartStickies Workflow Automation Tool

This Smart Stickies Workflow Automation Tool is designed to dynamically generate user interfaces (UIs) based on user prompts, using LLAMA models to interpret requirements and render corresponding HTML code from an existing database of UI APIs. This documentation provides an overview of the project's structure, setup instructions, and usage guidelines.

# Project Overview
The application allows users to input specific UI requirements through a web form. These inputs are processed by an AI model that interprets the prompts and generates the appropriate HTML code. The generated code is then displayed within a phone emulator on the web page, providing a visual representation of the requested UI.

# Repository Structure
The repository consists of the following key files and directories:

```app.py```: The main Flask application file that handles routing and integrates with the AI model.
api_database.json: A JSON file containing a database of APIs used for UI element generation.
customer_preferences.json: A JSON file storing customer-specific preferences to tailor the UI generation process.
templates/: Directory containing HTML templates for rendering web pages.
static/: Directory for static files such as CSS stylesheets.
requirements.txt: A file listing the Python dependencies required to run the application.
Setup Instructions
To set up and run the Smart Stickies Workflow application locally, follow these steps:

Clone the Repository:

```bash
git clone https://github.com/UjjwalKaur/smart-stickies-workflow.git
```

Navigate to the Project Directory:

```bash
cd smart-stickies-workflow
```

Create and Activate a Virtual Environment:

```bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install Dependencies:
```
```bash
pip install -r requirements.txt
```

Set Up Environment Variables: Create a .env file in the project root directory and add the following line, replacing ```YOUR_GROQ_API_KEY``` with your actual API key:

```GROQ_API_KEY=YOUR_GROQ_API_KEY```

Run the Application:

```bash
python app.py
```
The application will start, and you can access it by navigating to http://127.0.0.1:5000 in your web browser.

## Usage
Once the application is running:

Access the Web Interface: Open your web browser and go to http://127.0.0.1:5000.

Input User Requirements: Fill in the "Customer Name" and "User Prompt" fields with the desired UI specifications.

Generate the UI: Click the "Generate Website" button. The application will process the input and display the generated HTML code within the phone emulator on the page.
