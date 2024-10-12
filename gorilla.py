import json 
import torch
import os 
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

access_token = os.getenv("HUGGINGFACE_TOKEN")
login(token= access_token)

tokenizer = AutoTokenizer.from_pretrained("gorilla-llm/gorilla-openfunctions-v2")
model = AutoModelForCausalLM.from_pretrained("gorilla-llm/gorilla-openfunctions-v2")


prompt = 'Fetch an API to create a Submit Button and a Checkbox'
inputs = tokenizer(prompt, return_tensors= 'pt')

outputs = model.generate(**inputs, max_length=150)
response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response_text)