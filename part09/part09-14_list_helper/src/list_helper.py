# WRITE YOUR SOLUTION HERE:
from collections import Counter

class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        numbers = ListHelper.create_dict(my_list)
        greatest = 0
        for key, value in numbers.items():
            if value > greatest:
                most_repeated = key
                greatest = value
        return most_repeated
    
    @classmethod
    def doubles(cls, my_list: list):
        numbers = ListHelper.create_dict(my_list)
        duplicates = 0
        for key, value in numbers.items():
            if value >= 2:
                duplicates += 1
        return duplicates
    
    @classmethod
    def create_dict (cls, my_list:list):
        numbers = {}
        for i in my_list:
            if i not in numbers:
                numbers[i] = 1
            else:
                numbers[i] += 1
        return numbers

