import requests
from bs4 import BeautifulSoup

def get_prices_from_skapiec(url, headers, product_name, store):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product_boxes = soup.find_all('div', class_='product-box-wide-d')
    prices = []
    for box in product_boxes:
        title_tag = box.find('h2', class_='product-box-wide-d-main__title')
        price_tag = box.find('span', class_='price price--secondary price--fw-500 price--fs-16')
        
        if title_tag and price_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip().replace('zł', '').replace(' ', '').replace(',', '.')
            
            if product_name.lower() in title.lower():
                prices.append((title, float(price), store))
    return prices

def get_prices_from_ceneo(url, headers, product_name, store):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product_boxes = soup.find_all('div', class_='cat-prod-row')
    prices = []
    for box in product_boxes:
        title_tag = box.find('a', class_='go-to-product')
        price_tag = box.find('span', class_='price')
        
        if title_tag and price_tag:
            title = title_tag.get('title', '').strip()
            price = price_tag.text.strip().replace('zł', '').replace(' ', '').replace(',', '.')
            
            if product_name.lower() in title.lower():
                prices.append((title, float(price), store))
    return prices

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

product_name = "iPhone"
urls = {
    "Ceneo": "https://www.ceneo.pl/Smartfony",
    "Skąpiec": "https://www.skapiec.pl/cat/26136-smartfony.html"
}

all_prices = []

for store, url in urls.items():
    try:
        if "ceneo" in url:
            prices = get_prices_from_ceneo(url, headers, product_name, store)
        else:
            prices = get_prices_from_skapiec(url, headers, product_name, store)
        
        if prices:
            all_prices.extend(prices)
            for title, price, store in prices:
                print(f"{store}: {title} - {price} zł")
        else:
            print(f"{store}: Produkt '{product_name}' nie znaleziony.")
    except Exception as e:
        print(f"Błąd przy pobieraniu danych ze sklepu {store}: {e}")

if all_prices:
    cheapest_product = min(all_prices, key=lambda x: x[1])
    print(f"\nNajtańsza oferta: {cheapest_product[0]} - {cheapest_product[1]} zł (Sklep: {cheapest_product[2]})")
else:
    print("\nNie znaleziono żadnych ofert dla podanego produktu.")