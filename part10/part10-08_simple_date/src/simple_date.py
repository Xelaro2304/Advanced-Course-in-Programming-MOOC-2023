# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    def __set_date(self):
        concatenate_date = str(self.year)+str(self.month)+str(self.day)
        return int(concatenate_date)
    
    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'
    
    def __lt__(self, another):
        return self.__set_date() < another.__set_date()
    
    def __gt__(self, another):
        return self.__set_date() > another.__set_date()
    
    def __eq__(self, another):
        return self.__set_date() == another.__set_date()
    
    def __ne__(self, another):
        return self.__set_date() != another.__set_date()
    
    def __convert_to_date(self, number: int):
        other_year = (number) // 360
        other_month = ((number) % 360) // 30
        other_day = ((number) % 360) % 30
        return SimpleDate(other_day, other_month, other_year)
    
    def __convert_to_days(self):
        days = (self.year *360) + (self.month * 30)  + self.day
        return days
    
    def __add__(self, another: int):
        other_date = self.__convert_to_date(another)
        other_date.year += self.year
        other_date.month += self.month
        other_date.day += self.day

        if other_date.day > 30:
            other_date.day -= 30
            other_date.month += 1
        
        if other_date.month > 12:
            other_date.month -= 12
            other_date.year +=1
        return other_date
    
    def __sub__(self, another):
        other_date = another
        other_date.year = self.year - other_date.year
        other_date.month = self.month - other_date.month
        other_date.day = self.day - other_date.day

        difference = other_date.__convert_to_days()
        return abs(difference)
 