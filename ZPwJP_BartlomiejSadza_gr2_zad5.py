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
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

url = "https://www.cortland.pl/iphone/"
headers = {"User-Agent": "Mozilla/5.0"}

# Create a session
session = requests.Session()

# Define a retry strategy
retry_strategy = Retry(
    total=5,  # Number of retries
    backoff_factor=1,  # Wait time between retries
    status_forcelist=[429, 500, 502, 503, 504],  # Retry on these status codes
    method_whitelist=["HEAD", "GET", "OPTIONS"]  # Retry for these methods
)

# Mount the retry strategy to the session
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

try:
    response = session.get(url, headers=headers, timeout=10)  # Increase timeout
    response.raise_for_status()  # Raise an exception for HTTP errors
    prices = response.json()  # Assuming the response is in JSON format
    print(prices)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")