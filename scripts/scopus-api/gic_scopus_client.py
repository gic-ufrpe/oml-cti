import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELSEVIER_API_KEY")

BASE_URL = "https://api.elsevier.com/content/search/scopus"

def search_scopus(query: str, count: int = 5):
    headers = {
        "X-ELS-APIKey": API_KEY,
        "Accept": "application/json"
    }

    all_entries = []
    cursor = "*"

    while True:
        params = {
            "query": query,
            "count": count,
            "cursor": cursor,
            "view": "COMPLETE"
        }

        response = requests.get(BASE_URL, headers=headers, params=params)

        print("--- SCOPUS API Headers ---")
        print(response.headers)

        if response.status_code != 200:
            raise Exception(f"Erro na API: {response.status_code} - {response.text}")

        data = response.json()
        search_results = data.get("search-results", {})
        entries = search_results.get("entry", [])
        
        all_entries.extend(entries)
        
        next_cursor = search_results.get("cursor", {}).get("@next")
        
        if not next_cursor or next_cursor == cursor:
            break
            
        cursor = next_cursor

    return {"search-results": {"entry": all_entries}}