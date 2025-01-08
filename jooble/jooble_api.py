import requests
import pandas as pd
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


try:
    response = requests.post(url, headers={"Content-Type": "application/json"}, json=payload)
    response.raise_for_status() 
    data = response.json()
    
    print("Status:", response.status_code)
    print("Znalezione oferty pracy:")
    
    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            'title': job.get('title'),
            'location': job.get('location'),
            'snippet': job.get('snippet'),
            'salary': job.get('salary'),
            'source': job.get('source'),
            'type': job.get('type'),
            'link': job.get('link'),
            'company': job.get('company'),
            'updated': job.get('updated'),
            'id': job.get('id')
        })
        
    df_jooble = pd.DataFrame(jobs)
    print(df_jooble.head())


except requests.exceptions.RequestException as e:
    print(f"Błąd podczas wykonywania zapytania: {e}")
    
    