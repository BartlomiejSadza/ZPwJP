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
from textblob import TextBlob


def zadanie1():
    csv_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"

    csv_data = pd.read_csv(csv_url)
    print("CSV Data:")
    print(csv_data.head())

    zip_url = "https://www.contextures.com/tablesamples/sampledatafoodsales.zip"

    response = requests.get(zip_url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    with zip_file.open("sampledatafoodsales.xlsx") as file:
        zip_data = pd.read_excel(file, sheet_name="FoodSales")
        print("\nZIP Data:")
        print(zip_data.head())


# zadanie1()


def zadanie2():
    wiki_url = (
        "https://en.wikipedia.org/wiki/List_of_European_countries_by_life_expectancy"
    )
    response = requests.get(wiki_url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", {"class": "wikitable"})

    if table is None:
        print("Table not found")
    else:
        headers = [header.text.strip() for header in table.find_all("th")]
        rows = table.find_all("tr")[1:]

        data = []
        for row in rows:
            columns = row.find_all("td")
            if columns:
                data.append([column.text.strip() for column in columns])

        if len(data) > 0 and len(data[0]) != len(headers):
            headers = headers[: len(data[0])]

        life_expectancy_df = pd.DataFrame(data, columns=headers)
        print("\nOczekiwana długość zycia:")
        print(life_expectancy_df.head())


# zadanie2()


def zadanie3():
    start_date = "2024-07-01"
    end_date = "2024-10-01"

    currencies = ["USD", "EUR", "GBP"]

    def fetch_currency_data(currency, start_date, end_date):
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{start_date}/{end_date}/?format=json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Nie udało się pobrać danych dla {currency}")
            return None

    currency_data = {}
    for currency in currencies:
        data = fetch_currency_data(currency, start_date, end_date)
        if data:
            currency_data[currency] = data

    for currency, data in currency_data.items():
        rates = data.get("rates", [])
        df = pd.DataFrame(rates)
        df["effectiveDate"] = pd.to_datetime(df["effectiveDate"])
        df.set_index("effectiveDate", inplace=True)
        print(f"\n{currency} Aktualny kurs:")
        print(df.head())


# zadanie3()


def zadanie4():
    chrome_driver_path = "/opt/homebrew/bin/chromedriver"

    chrome_service = Service(chrome_driver_path)

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def scrape_table(url):
        driver.get(url)
        time.sleep(4)
        table = driver.find_element(By.TAG_NAME, "table")
        headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]
        rows = table.find_elements(By.TAG_NAME, "tr")[1:]
        data = []
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            data.append([column.text for column in columns])
        return headers, data

    url = "https://www.polskawliczbach.pl/najszybciej_wyludniajace_sie_miasta_w_polsce"
    headers, data = scrape_table(url)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(data, columns=headers)
    file_name = "wyludniajace_sie_miasta.csv"
    df.to_csv(file_name, index=False)
    print(f"Dane zapisano w pliku: {file_name}")

    driver.quit()


# zadanie4()


def zadanie5():
    def get_prices_from_skapiec(url, headers, product_name, store):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        product_boxes = soup.find_all("div", class_="product-box-wide-d")
        prices = []
        for box in product_boxes:
            title_tag = box.find("h2", class_="product-box-wide-d-main__title")
            price_tag = box.find(
                "span", class_="price price--secondary price--fw-500 price--fs-16"
            )

            if title_tag and price_tag:
                title = title_tag.text.strip()
                price = (
                    price_tag.text.strip()
                    .replace("zł", "")
                    .replace(" ", "")
                    .replace(",", ".")
                )

                if product_name.lower() in title.lower():
                    prices.append((title, float(price), store))
        return prices

    def get_prices_from_ceneo(url, headers, product_name, store):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        product_boxes = soup.find_all("div", class_="cat-prod-row")
        prices = []
        for box in product_boxes:
            title_tag = box.find("a", class_="go-to-product")
            price_tag = box.find("span", class_="price")

            if title_tag and price_tag:
                title = title_tag.get("title", "").strip()
                price = (
                    price_tag.text.strip()
                    .replace("zł", "")
                    .replace(" ", "")
                    .replace(",", ".")
                )

                if product_name.lower() in title.lower():
                    prices.append((title, float(price), store))
        return prices

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

    product_name = "iPhone"
    urls = {
        "Ceneo": "https://www.ceneo.pl/Smartfony",
        "Skąpiec": "https://www.skapiec.pl/cat/26136-smartfony.html",
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
        print(
            f"\nNajtańsza oferta: {cheapest_product[0]} - {cheapest_product[1]} zł (Sklep: {cheapest_product[2]})"
        )
    else:
        print("\nNie znaleziono żadnych ofert dla podanego produktu.")


# zadanie5()


def zadanie6():
    def get_headlines(url, category, headers):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("h3")
        headlines_text = [headline.text.strip() for headline in headlines[:5]]

        return [
            {"kategoria": category, "naglowek": headline} for headline in headlines_text
        ]

    sources = {
        "BBC Sport": ("https://www.bbc.com/sport", "sport"),
        "BBC Politics": ("https://www.bbc.com/news/politics", "polityka"),
        "CNN Sport": ("https://edition.cnn.com/sport", "sport"),
        "CNN Politics": ("https://edition.cnn.com/politics", "polityka"),
        "Onet Sport": ("https://sport.onet.pl", "sport"),
        "Onet Politics": ("https://wiadomosci.onet.pl/polityka", "polityka"),
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

    all_headlines = []

    for name, (url, category) in sources.items():
        try:
            headlines = get_headlines(url, category, headers)
            all_headlines.extend(headlines)
            print(f"Pobrano nagłówki z {name}")
        except Exception as e:
            print(f"Błąd przy pobieraniu danych z {name}: {e}")

    df = pd.DataFrame(all_headlines)
    df.set_index("kategoria", inplace=True)
    print(df)

    file_name = "naglowki.csv"
    df.to_csv(file_name, index=False)

    print("")
    print(f"Zapisano nagłówki do pliku: {file_name}")


zadanie6()


def zadanieD1():
    from datetime import datetime
    import time

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_flight_price(url, origin, destination, date):
        driver.get(url)
        time.sleep(5)  # zeby strona sie zaladowala

        prices = []
        try:
            price_elements = driver.find_elements(By.CLASS_NAME, "price-class")
            for price_element in price_elements:
                prices.append(price_element.text.strip())
        except Exception as e:
            print(f"Błąd pobierania cen: {e}")

        prices_data = [
            {
                "origin": origin,
                "destination": destination,
                "date_checked": datetime.now(),
                "price": price,
            }
            for price in prices
        ]
        return prices_data

    url = "https://www.kayak.pl/"
    origin = "KRK"
    destination = "JFK"
    date = "2024-11-01"

    prices_data = get_flight_price(url, origin, destination, date)
    df = pd.DataFrame(prices_data)
    file_name = f"flight_prices_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(file_name, index=False)
    print(f"Ceny zapisano w pliku: {file_name}")

    driver.quit()


# zadanieD1()


def zadanieD2():
    def get_movie_reviews(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        reviews = []
        review_elements = soup.find_all("div", class_="text show-more__control")
        for review_element in review_elements:
            reviews.append(review_element.text.strip())

        return reviews

    def analyze_sentiment(reviews):
        sentiments = []
        for review in reviews:
            blob = TextBlob(review)
            sentiments.append(blob.sentiment.polarity)
        return sentiments

    def summarize_reviews(reviews, sentiments):
        df = pd.DataFrame({"Review": reviews, "Sentiment": sentiments})
        average_sentiment = df["Sentiment"].mean()
        return df, average_sentiment

    url = "https://www.imdb.com/title/tt0111161/reviews"  # Skazani na Showshank :D
    reviews = get_movie_reviews(url)
    sentiments = analyze_sentiment(reviews)
    df, average_sentiment = summarize_reviews(reviews, sentiments)

    file_name = "movie_reviews.csv"
    df.to_csv(file_name, index=False)
    print(f"Recenzje zapisano w pliku: {file_name}")
    print(f"Średnia ocena sentymentu: {average_sentiment}")


# zadanieD2()


def zadanieD5(team):
    def get_team_stats(url, team_name):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the table containing the match data
        table = soup.find(
            "table", {"class": "some-class-name"}
        )  # Adjust the selector as needed
        if table is None:
            print("Table not found")
            return None

        rows = table.find("tbody").find_all("tr")

        data = []
        for row in rows:
            columns = row.find_all("td")
            if len(columns) > 0:
                position = columns[0].text.strip()
                team = columns[2].text.strip()
                matches_played = columns[3].text.strip()
                wins = columns[4].text.strip()
                draws = columns[5].text.strip()
                losses = columns[6].text.strip()
                goals_for = columns[7].text.strip()
                goals_against = columns[8].text.strip()
                goal_difference = columns[9].text.strip()
                points = columns[10].text.strip()

                if team_name.lower() in team.lower():
                    data.append(
                        {
                            "position": position,
                            "team": team,
                            "matches_played": matches_played,
                            "wins": wins,
                            "draws": draws,
                            "losses": losses,
                            "goals_for": goals_for,
                            "goals_against": goals_against,
                            "goal_difference": goal_difference,
                            "points": points,
                        }
                    )

        return data

    def calculate_statistics(data, team_name):
        total_matches = len(data)
        wins = 0
        losses = 0
        draws = 0

        for match in data:
            wins += int(match["wins"])
            losses += int(match["losses"])
            draws += int(match["draws"])

        return {
            "total_matches": total_matches,
            "wins": wins,
            "losses": losses,
            "draws": draws,
        }

    url = "https://footystats.org/spain/la-liga"
    team_name = team

    match_data = get_team_stats(url, team_name)
    df = pd.DataFrame(match_data)

    print("DataFrame columns:", df.columns)
    print("First few rows of the DataFrame:\n", df.head())

    if "team" in df.columns:
        df.set_index("team", inplace=True)
    else:
        print("Column 'team' not found in DataFrame")

    file_name = f"{team_name}_matches.csv"
    df.to_csv(file_name, index=True)
    print(f"Wyniki zapisano w pliku: {file_name}")

    stats = calculate_statistics(match_data, team_name)
    print(f"Statystyki dla {team_name}:")
    print(f"Total Matches: {stats['total_matches']}")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    print(f"Draws: {stats['draws']}")


# zadanieD5("Fc Barcelona")


# To było dla mnie mega trudne i czasochłonne, więc silnie wspierane przez AI.
# Pozdrawiam serdecznie 
