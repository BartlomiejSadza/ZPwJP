import requests
import time

BASE_URL = "https://api.justjoin.it/v2/user-panel/offers/by-cursor"
# https://api.justjoin.it/v2/user-panel/offers/by-cursor?currency=pln&from=100&itemsCount=100&orderBy=DESC&sortBy=published

def fetch_all_offers():
    all_offers = []
    offset = 0            # od którego rekordu startujemy
    chunk_size = 100      # ile ofert pobieramy na jeden request
    
    while len(all_offers) < 100:
        params = {
            "currency": "pln",
            "from": offset,
            "itemsCount": 100,
            "orderBy": "DESC",
            "sortBy": "published"
        }
        
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        offers = data['data']
        all_offers.extend(offers)
        
        meta = data['meta']
        next_ = meta['next']        # np. {"cursor": 400, "itemsCount": 100}
        next_offset = next_['cursor']   # kolejny offset (np. 400)
        fetched_count = len(offers)
        
        print(f"Offset={offset}, pobrano {fetched_count} ofert. nextOffset={next_offset}")

        # Jeśli API zwraca 0 ofert lub brak next_offset, to kończymy
        if fetched_count == 0 or not next_offset:
            break
        
        # Przechodzimy do kolejnej „strony”
        offset = next_offset
        
        # Drobny sleep, żeby nie walić requestami co milisekundę
        time.sleep(0.5)
    
    # zwracamy albo 100, albo tyle ile faktycznie udało się pobrać
    return all_offers[:100]

if __name__ == "__main__":
    offers = fetch_all_offers()
    print(f"Łącznie pobrano {len(offers)} ofert.")