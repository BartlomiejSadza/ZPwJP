import pytest
from zadania_Testowanie import BankAccount, TaskManager, ReservationSystem


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