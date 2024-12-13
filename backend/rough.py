from datetime import datetime
import requests

url = "http://127.0.0.1:40069/add-movie"

headers = {
    'Content-type': 'application/json',
    'Accept': 'text/plain'
}

# Use ISO format directly as a string (this matches what FastAPI expects)
payload = {
    'name': 'Hari Potir',
    'description': 'Ron is waste',
    'release_date': '2002-02-02'
}

res = requests.post(url, json=payload, headers=headers)
print(res.status_code)
print(res.content)