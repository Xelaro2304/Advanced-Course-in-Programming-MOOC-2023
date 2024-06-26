# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if len(self.numbers) != 0:
            return sum(self.numbers)
        else:
            return 0
    
    def average(self):
        if len(self.numbers) != 0:
            return sum(self.numbers)/len(self.numbers)
        else:
            return 0


stats = NumberStats()
even = NumberStats()
odd = NumberStats()
while True:
    number = int(input('Number:'))
    if number == -1:
        break
    elif number%2 == 0:
        stats.add_number(number)
        even.add_number(number)
    elif number%2 == 1:
        stats.add_number(number)
        odd.add_number(number)

print(f'Sum of numbers: {stats.get_sum()}')
print(f'Mean of numbers: {stats.average()}')
print(f'Sum of even numbers: {even.get_sum()}')
print(f'Sum of odd numbers: {odd.get_sum()}')
