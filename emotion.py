import tkinter as tk
import requests


API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
API_KEY = "Hidden"  

def query_huggingface_api(text):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()

def adjust_interface_on_emotion():
    user_input = entry.get()
    result = query_huggingface_api(user_input)
    
    emotion = result[0][0]["label"]  
    
    if emotion == "POSITIVE":
        result_label.config(text="Positive emotion detected!", bg="lightgreen")
    elif emotion == "NEGATIVE":
        result_label.config(text="Negative emotion detected!", bg="lightcoral")
    else:
        result_label.config(text="Neutral emotion", bg="lightyellow")

root = tk.Tk()
root.title("Dynamic UI with AI")
root.geometry("800x400")

entry_label = tk.Label(root, text="Enter some text:")
entry_label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

analyze_button = tk.Button(root, text="Analyze Emotion", command=adjust_interface_on_emotion)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="", width=800, height=400)
result_label.pack(pady=10)

root.mainloop()