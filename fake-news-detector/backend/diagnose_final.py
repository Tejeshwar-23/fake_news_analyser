import requests

url = "http://127.0.0.1:5000/api/predict"
headline = "'Not heard from anyone except Trump': Lavrov on US claims of India halting Russian oil imports"

variations = [
    ("Original", headline),
    ("Lowercase", headline.lower()),
    ("No Single Quotes", headline.replace("'", "")),
    ("With Reuters Prefix", "NEW DELHI (Reuters) - " + headline)
]

for label, v in variations:
    res = requests.post(url, json={"text": v}).json()
    print(f"[{label}]: {res.get('prediction')}")
