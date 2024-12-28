import requests

url = "https://api.justjoin.it/v2/user-panel/offers/by-cursor"
params = {
    "currency": "pln",
    "orderBy": "DESC",
    "sortBy": "published"
    # można dodać np. "cursor": "..." jeśli endpoint obsługuje paginację
}

headers = {
    "User-Agent": "Mozilla/5.0",
    # ewentualnie jeszcze Accept: "application/json", itp.
}

response = requests.get(url, params=params, headers=headers)
response.raise_for_status()

data = response.json()
# print(data)