
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
    
