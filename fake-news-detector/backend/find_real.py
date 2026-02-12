import requests
import json

url = "http://127.0.0.1:5000/api/predict"

samples = [
    "WASHINGTON (Reuters) - The U.S. Congress on Friday approved a massive spending bill to keep the government running through the end of the fiscal year.",
    "LONDON (Reuters) - Prime Minister Theresa May's government will not hold a vote on her Brexit deal in parliament on Tuesday.",
    "The sun rises in the east and sets in the west.",
    "Python is a high-level, general-purpose programming language.",
    "A cat sat on the mat."
]

for text in samples:
    try:
        response = requests.post(url, json={"text": text})
        print(f"Text: {text[:50]}...")
        print(f"Prediction: {response.json().get('prediction')}")
        print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")
