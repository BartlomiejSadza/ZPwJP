import pandas as pd
import requests
import zipfile
import io
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# csv_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"

# csv_data = pd.read_csv(csv_url)
# # print("CSV Data:")
# # print(csv_data.head())

# zip_url = "https://www.contextures.com/tablesamples/sampledatafoodsales.zip"

# response = requests.get(zip_url)
# zip_file = zipfile.ZipFile(io.BytesIO(response.content))

# with zip_file.open('sampledatafoodsales.xlsx') as file:
#     zip_data = pd.read_excel(file, sheet_name="FoodSales")
#     # print("\nZIP Data:")
#     # print(zip_data.head())

# wiki_url = "https://en.wikipedia.org/wiki/List_of_European_countries_by_life_expectancy"
# response = requests.get(wiki_url)
# soup = BeautifulSoup(response.content, 'html.parser')

# table = soup.find('table', {'class': 'wikitable'})

# if table is None:
#     print("Table not found")
# else:
#     headers = [header.text.strip() for header in table.find_all('th')]
#     rows = table.find_all('tr')[1:]

#     data = []
#     for row in rows:
#         columns = row.find_all('td')
#         if columns:
#             data.append([column.text.strip() for column in columns])

#     if len(data) > 0 and len(data[0]) != len(headers):
#         headers = headers[:len(data[0])]

#     life_expectancy_df = pd.DataFrame(data, columns=headers)
#     # print("\nLife Expectancy Data:")
#     # print(life_expectancy_df.head())

# # Define the date range
# start_date = "2024-07-01"
# end_date = "2024-10-01"

# # Define the currency codes you want to fetch
# currencies = ["USD", "EUR", "GBP"]

# # Function to fetch data from NBP API
# def fetch_currency_data(currency, start_date, end_date):
#     url = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{start_date}/{end_date}/?format=json"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed to fetch data for {currency}")
#         return None

# # Fetch data for each currency
# currency_data = {}
# for currency in currencies:
#     data = fetch_currency_data(currency, start_date, end_date)
#     if data:
#         currency_data[currency] = data

# # Process and display the data
# for currency, data in currency_data.items():
#     rates = data.get("rates", [])
#     df = pd.DataFrame(rates)
#     df["effectiveDate"] = pd.to_datetime(df["effectiveDate"])
#     df.set_index("effectiveDate", inplace=True)
#     # print(f"\n{currency} Exchange Rates:")
#     # print(df.head())


# Zadanie 4 ####################################################################################################

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# # Set the path to the ChromeDriver executable
# chrome_driver_path = "/opt/homebrew/bin/chromedriver"  # Update this path

# # Create a Service object with the path to ChromeDriver
# chrome_service = Service(chrome_driver_path)

# # Set Chrome options if needed
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode if needed

# # Initialize the WebDriver
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# # Function to scrape data from a given URL
# def scrape_table(url):
#     driver.get(url)
#     time.sleep(3)  # Wait for the page to load
#     table = driver.find_element(By.TAG_NAME, 'table')
#     headers = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
#     rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
#     data = []
#     for row in rows:
#         columns = row.find_elements(By.TAG_NAME, 'td')
#         data.append([column.text for column in columns])
#     return headers, data

# # Example usage
# url = "https://example.com/table"
# headers, data = scrape_table(url)
# print(headers)
# print(data)

# # Don't forget to quit the driver
# driver.quit()

####################################################################################################

# Zadanie 6
# Funkcja do pobierania nagłówków z danego URL i kategorii
# def get_headlines(url, category, headers):
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Przykładowe selektory (dostosuj do konkretnej strony)
#     headlines = soup.find_all('h3')  # Na przykład: wyszukujemy wszystkie nagłówki h3
#     headlines_text = [headline.text.strip() for headline in headlines[:5]]  # Pobieramy pierwsze 5 nagłówków

#     return [{"kategoria": category, "naglowek": headline} for headline in headlines_text]

# # Przykładowe linki do stron z kategoriami sport i polityka (zmień na rzeczywiste URL-e serwisów)
# sources = {
#     "BBC Sport": ("https://www.bbc.com/sport", "sport"),
#     "BBC Politics": ("https://www.bbc.com/news/politics", "polityka"),
#     "CNN Sport": ("https://edition.cnn.com/sport", "sport"),
#     "CNN Politics": ("https://edition.cnn.com/politics", "polityka"),
#     "Onet Sport": ("https://sport.onet.pl", "sport"),
#     "Onet Politics": ("https://wiadomosci.onet.pl/polityka", "polityka")
# }

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
# }

# # Pobieranie nagłówków z każdej strony i kategorii
# all_headlines = []

# for name, (url, category) in sources.items():
#     try:
#         headlines = get_headlines(url, category, headers)
#         all_headlines.extend(headlines)
#         print(f"Pobrano nagłówki z {name}")
#     except Exception as e:
#         print(f"Błąd przy pobieraniu danych z {name}: {e}")

# # Organizacja danych w DataFrame i zapis do pliku CSV
# df = pd.DataFrame(all_headlines)
# df.set_index("kategoria", inplace=True)
# print(df)

# file_name = "naglowki.csv"
# df.to_csv(file_name, index=False)

# print("")
# print(f"Zapisano nagłówki do pliku: {file_name}")

####################################################################################################

# zadanie D1 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import pandas as pd
from datetime import datetime
import time

# Inicjalizacja przeglądarki
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def get_flight_price(url, origin, destination, date):
    # Załaduj stronę z wynikami lotów
    driver.get(url)
    time.sleep(3)  # Czas na załadowanie strony

    # Przykład pobierania danych z elementu na stronie (dostosuj selektory do konkretnej strony)
    prices = []
    try:
        price_elements = driver.find_elements(By.CLASS_NAME, "price-class")  # Zamień "price-class" na odpowiedni selektor
        for price_element in price_elements:
            prices.append(price_element.text.strip())
    except Exception as e:
        print(f"Błąd pobierania cen: {e}")
    
    # Zapisanie cen z datą sprawdzenia
    prices_data = [{"origin": origin, "destination": destination, "date_checked": datetime.now(), "price": price} for price in prices]
    return prices_data

# Parametry lotu
url = "https://www.kayak.pl/"
origin = "KRK"  # Lotnisko wylotu (np. Kraków)
destination = "JFK"  # Lotnisko docelowe (np. Nowy Jork)
date = "2024-11-15"

# Pobranie i zapisanie danych
prices_data = get_flight_price(url, origin, destination, date)
df = pd.DataFrame(prices_data)
file_name = f"flight_prices_{datetime.now().strftime('%Y%m%d')}.csv"
df.to_csv(file_name, index=False)
print(f"Ceny zapisano w pliku: {file_name}")

# Zamknij przeglądarkę
driver.quit()
