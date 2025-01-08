import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
HOST = 'https://pl.jooble.org'
API_KEY = os.getenv('API_KEY')


url = f"{HOST}/api/{API_KEY}"


payload = {
    "keywords": "it",
    "location": "Kraków"
}

# Wysłanie zapytania POST
try:
    response = requests.post(url, headers={"Content-Type": "application/json"}, json=payload)
    response.raise_for_status()  # Wykrywanie błędów HTTP
    data = response.json()

    # Wyświetlanie wyników
    print("Status:", response.status_code)
    print("Znalezione oferty pracy:")
    for job in data.get("jobs", []):
        print(job)
        print("-" * 40)

except requests.exceptions.RequestException as e:
    print(f"Błąd podczas wykonywania zapytania: {e}")