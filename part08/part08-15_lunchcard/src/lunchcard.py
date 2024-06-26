# Write your solution here:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f'The balance is {self.balance:.1f} euros'
    
    def eat_lunch(self):
        self.balance -= 2.60
        if self.balance < 0:
           self.balance += 2.60 

    def eat_special(self):
        self.balance -= 4.60
        if self.balance < 0:
           self.balance += 4.60
        
    def deposit_money(self, money):
        if money<0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += money

peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
print(f'Peter: {peters_card}')
graces_card.eat_lunch()
print(f'Grace: {graces_card}')
peters_card.deposit_money(20)
print(f'Peter: {peters_card}')
graces_card.eat_special()
print(f'Grace: {graces_card}')
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')
