# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, numbers: list) -> None:
        self.week = week
        self.numbers = numbers

    def number_of_hits(self, numbers:list):
        return len([number for number in numbers if number in self.numbers])

    def hits_in_place(self, numbers):
        return [number if number in self.numbers else -1 for number in numbers]
    
