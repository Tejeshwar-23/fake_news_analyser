import requests
import json

url = "http://127.0.0.1:5000/api/predict"
headline = "'Not heard from anyone except Trump': Lavrov on US claims of India halting Russian oil imports"

variations = [
    headline,
    "MOSCOW (Reuters) - " + headline,
    "NEW DELHI (Reuters) - " + headline
]

for text in variations:
    try:
        response = requests.post(url, json={"text": text})
        print(f"Text: {text[:60]}...")
        print(f"Prediction: {response.json().get('prediction')}")
        print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")
