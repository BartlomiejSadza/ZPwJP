import requests

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