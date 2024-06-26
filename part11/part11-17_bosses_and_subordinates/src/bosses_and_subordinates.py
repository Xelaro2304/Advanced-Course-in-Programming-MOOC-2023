# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    if employee.subordinates == []:
        return 0
    
    subordinates = len(employee.subordinates)
    for subordinate in employee.subordinates:
        subordinates += count_subordinates(subordinate)
    return subordinates