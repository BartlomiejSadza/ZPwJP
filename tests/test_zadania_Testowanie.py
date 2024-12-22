import pytest
from unittest.mock import patch, Mock
import requests
from hypothesis import given, strategies as st
from zadania_Testowanie import BankAccount, Book, Calculator, Library, TaskManager, ReservationSystem, User, fetch_user_data, aggregate_weather_data, is_sorted


# zadanie 1
@pytest.fixture
def task_manager():
    return TaskManager()

def test_add_mark_complete_remove_task(task_manager: TaskManager):
    # Dodawanie tasku
    task_manager.add_task(1, "Test Task")
    assert 1 in task_manager.tasks
    assert task_manager.tasks[1]['name'] == 'Test Task'
    assert not task_manager.tasks[1]['completed']

    # Oznaczanie jako wykonany
    task_manager.mark_task_completed(1)
    assert task_manager.tasks[1]['completed']

    # usuwanie tasku 
    task_manager.remove_task(1)
    assert 1 not in task_manager.tasks


# zadanie 2
@pytest.fixture
def reservation_system():
    return ReservationSystem()

def test_reserve_cancel_seat(reservation_system: ReservationSystem):
    #Rezerwacja miejsca 
    reservation_system.reserve_seat(1)
    assert reservation_system.is_seat_reserved(1)

    # Anulowanie rezerwacji
    reservation_system.cancel_reservation(1)
    assert not reservation_system.is_seat_reserved(1)

def test_double_reservation(reservation_system: ReservationSystem):
    reservation_system.reserve_seat(1)
    assert reservation_system.is_seat_reserved(1)
    
    with pytest.raises(ValueError):
        reservation_system.reserve_seat(1)


# Zadanie 4
@pytest.fixture
def bank_account():
    return BankAccount()

def test_deposit(bank_account):
    bank_account.deposit(100)
    assert bank_account.balance == 100

def test_withdraw(bank_account):
    bank_account.deposit(100)
    bank_account.withdraw(50)
    assert bank_account.balance == 50

def test_withdraw_insufficient(bank_account):
    bank_account.deposit(100)
    with pytest.raises(ValueError, match="Nie masz wystarczających środków"):
        bank_account.withdraw(150)

def test_deposit_negative_amount(bank_account):
    with pytest.raises(ValueError, match="Wpłata musi być dodatnia xD"):
        bank_account.deposit(-50)

def test_withdraw_negative_amount(bank_account):
    with pytest.raises(ValueError, match="Wypłata musi być dodatnia"):
        bank_account.withdraw(-50)



# Zadanie 5
@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (1.5, 2.5, 4.0)
])
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (1, 1, 0),
    (2.5, 1.5, 1.0)
])
def test_subtract(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 1, -1),
    (1.5, 2, 3.0)
])
def test_multiply(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (1, 1, 1),
    (2.5, 0.5, 5.0)
])
def test_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(1, 0)


# zadanie 6
@pytest.mark.parametrize("name, email", [
    ("John", "john@example.com"),
    ("Jane", "jane@example.com")
])
def test_user_initialization(name, email):
    user = User(name, email)
    assert user.name == name
    assert user.email == email

@pytest.mark.parametrize("name, expected_greeting", [
    ("John", "Hello, John!"),
    ("Jane", "Hello, Jane!")
])
def test_user_greet(name, expected_greeting):
    user = User(name, "test@example.com")
    assert user.greet() == expected_greeting


# zadanie 7
@pytest.fixture
def library():
    return Library()

@pytest.fixture
def book():
    return Book("Test Title", "Test Author", 2021)

def test_add_book(library, book):
    library.add_book(book)
    assert library.find_book("Test Title") == book

def test_find_book(library, book):
    library.add_book(book)
    found_book = library.find_book("Test Title")
    assert found_book is not None
    assert found_book.title == "Test Title"
    assert found_book.author == "Test Author"
    assert found_book.year == 2021

def test_find_nonexistent_book(library):
    assert library.find_book("Nonexistent Title") is None


# zadanie 8
@patch('zadania_Testowanie.requests.get')
def test_fetch_user_data_success(mock_get):
    mock_response = Mock()
    expected_data = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
    mock_response.json.return_value = expected_data
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    user_data = fetch_user_data(1)
    assert user_data == expected_data

@patch('zadania_Testowanie.requests.get')
def test_fetch_user_data_connection_error(mock_get):
    mock_get.side_effect = requests.ConnectionError

    with pytest.raises(requests.ConnectionError):
        fetch_user_data(1)

@patch('zadania_Testowanie.requests.get')
def test_fetch_user_data_incomplete_data(mock_get):
    mock_response = Mock()
    incomplete_data = {'id': 1, 'name': 'John Doe'}
    mock_response.json.return_value = incomplete_data
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    user_data = fetch_user_data(1)
    assert user_data == incomplete_data


# Zadanie 9 
@patch('zadania_Testowanie.requests.get')
def test_aggregate_weather_data_success(mock_get):
    mock_response = Mock()
    expected_data = {"temperature": 20, "humidity": 50}
    mock_response.json.return_value = expected_data
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    cities = ['City1', 'City2']
    weather_data = aggregate_weather_data(cities)
    assert weather_data['City1'] == expected_data
    assert weather_data['City2'] == expected_data

@patch('zadania_Testowanie.requests.get')
def test_aggregate_weather_data_fail(mock_get):
    def side_effect(url):
        if "City1" in url:
            mock_response = Mock()
            mock_response.json.return_value = {"temperature": 20, "humidity": 50}
            mock_response.status_code = 200
            return mock_response
        else:
            raise requests.RequestException
        
    mock_get.side_effect = side_effect

    cities = ['City1', 'City2']
    weather_data = aggregate_weather_data(cities)
    assert weather_data['City1'] == {"temperature": 20, "humidity": 50}
    assert weather_data['City2'] is None


# Zadanie 10
@given(st.lists(st.integers()))
def test_is_sorted_random_listz(lst):
    sorted_lst = sorted(lst)
    assert is_sorted(sorted_lst) 

@given(st.lists(st.integers()))
def test_is_sorted_unsorted_lists(lst):
    assert is_sorted(lst) == (lst == sorted(lst))

@given(st.lists(st.integers(), min_size=100, max_size=10000))
def test_is_sorted_large_lists(lst):
    sorted_lst = sorted(lst)
    assert is_sorted(sorted_lst)


# Zadanie 11