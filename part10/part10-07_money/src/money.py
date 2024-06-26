# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"
        else:
            return f"{self.__euros}.{self.__cents} eur"

    def __eq__ (self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __gt__ (self, another):
        if self.__euros > another.__euros:
            return True
        elif self.__euros == another.__euros:
            return self.__cents > another.__cents
        else:
            return False
    
    def __lt__ (self, another):
        if self.__euros < another.__euros:
            return True
        elif self.__euros == another.__euros:
            return self.__cents < another.__cents
        else:
            return False
    
    def __ne__(self, another):
        return self.__euros != another.__euros or self.__cents != another.__cents
    
    def __add__ (self, another):
        if self.__cents + another.__cents > 99:
            sum_cents = self.__cents + another.__cents
            convert_cents = str(sum_cents)
            convert_cents = convert_cents[1:]
            final_cents = int(convert_cents)
            sum_euro = self.__euros + another.__euros + 1
            addition = Money(sum_euro, final_cents)
            return addition
        else:
            sum_cents = self.__cents + another.__cents
            sum_euro = self.__euros + another.__euros
            addition = Money(sum_euro, sum_cents)
            return addition
    
    def __sub__ (self, another):
        if self.__cents - another.__cents < 0:
            sub_cents = 100 + self.__cents - another.__cents
            sub_euro = self.__euros - another.__euros - 1
            if sub_euro < 0:
                raise ValueError ('a negative result is not allowed')
            sub = Money(sub_euro, sub_cents)
            return sub
        else:
            sub_cents = self.__cents - another.__cents
            sub_euro = self.__euros - another.__euros
            if sub_euro < 0:
                raise ValueError ('a negative result is not allowed')
            sub = Money(sub_euro, sub_cents)
            return sub