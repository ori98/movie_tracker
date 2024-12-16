from datetime import datetime
import requests

def post_movie():
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

def get_movies(search_term: str) -> list:
    url = "http://127.0.0.1:40069/get-movie"

    res = []
    payload = {'search_term': search_term}

    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    res = requests.get(url, params=payload, headers=headers)

    print(res.json())
    return res

if __name__ == "__main__":
    get_movies('harri')