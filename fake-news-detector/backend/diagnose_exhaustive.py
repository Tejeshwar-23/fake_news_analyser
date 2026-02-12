import requests

url = "http://127.0.0.1:5000/api/predict"
headline = "'Not heard from anyone except Trump': Lavrov on US claims of India halting Russian oil imports"

variations = [
    headline,
    headline.lower(),
    headline.upper(),
    headline.strip("'"),
    headline.replace("'", ""),
    # Let's try some common Indian news phrases that might be in a fake news set
    headline + " #BreakingNews",
    headline + " Click here to read more!"
]

for v in variations:
    res = requests.post(url, json={"text": v}).json()
    print(f"Text: {v[:50]}... -> {res.get('prediction')}")
