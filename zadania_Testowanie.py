import requests
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Zadanie 1
class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, task_name):
        self.tasks[task_id] = {'name': task_name, 'completed': False}

    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

# Zadanie 2
class ReservationSystem: 
    def __init__(self):
        self.reservations = {}

    def reserve_seat(self, seat_number):
        if seat_number in self.reservations and self.reservations[seat_number]:
            raise ValueError("seat juz zajety!!")
        self.reservations[seat_number] = True

    def cancel_reservation(self, seat_number):
        if seat_number in self.reservations:
            self.reservations[seat_number] = False

    def is_seat_reserved(self, seat_number):
        return self.reservations.get(seat_number, False)
    
# Zadanie 4

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Wpłata musi być dodatnia xD")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Wypłata musi być dodatnia")
        if amount > self.balance:
            raise ValueError("Nie masz wystarczających środków")
        self.balance -= amount


# Zadanie 5
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Zadanie 6
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello, {self.name}!"


# Zadanie 7
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


#Zadanie 8
def fetch_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()


# ZAdanie 9
def aggregate_weather_data(cities):
    weather_data = {}
    for city in cities:
        try:
            response = requests.get(f"https://api.example.com/weather?city={city}")
            response.raise_for_status()
            weather_data[city] = response.json()
        except requests.RequestException:
            weather_data[city] = None
    return weather_data


# Zadanie 10
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


# Zadanie 11
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
        

# Zadanie 12 
def parallel_sum(data, n_threads):
    def chunked_sum(chunk):
        return sum(chunk)

    chunk_size = len(data) // n_threads
    chunks = [data[i * chunk_size: (i + 1) * chunk_size] for i in range(n_threads)]

    if len(data) % n_threads != 0:
        chunks.append(data[n_threads * chunk_size:])

    with ThreadPoolExecutor(max_workers=n_threads) as egzekutor:
        results = egzekutor.map(chunked_sum, chunks)

    return sum(results)


# damn, te zadania mogłyby być osobnym projektem xD 