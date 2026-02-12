import requests

url = "http://127.0.0.1:5000/api/predict"
headline = "'Not heard from anyone except Trump': Lavrov on US claims of India halting Russian oil imports"

def test(text):
    res = requests.post(url, json={"text": text}).json()
    print(f"Prediction for '{text[:40]}...': {res.get('prediction')}")

test(headline)
test("WASHINGTON (Reuters) - " + headline)
