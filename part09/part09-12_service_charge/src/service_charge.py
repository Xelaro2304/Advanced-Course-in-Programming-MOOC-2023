# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, account_nmbr: str, balance: float):
        self.__owner = owner
        self.__account = account_nmbr
        self.__balance = balance
    
    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount:float):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance -= self.__balance*0.01