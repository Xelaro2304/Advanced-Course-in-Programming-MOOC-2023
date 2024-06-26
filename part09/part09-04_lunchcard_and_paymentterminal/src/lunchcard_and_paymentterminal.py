# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        self.balance -= amount
        if self.balance < 0:
            self.balance += amount
            return False
        else:
            return True
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        payment -= 2.50
        if payment < 0:
            return payment + 2.50 
        else:
            self.funds += 2.50
            self.lunches += 1
            return payment 
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
    

    def eat_special(self, payment: float):
        payment -= 4.30
        if payment < 0:
            return payment  + 4.3
        else:
            self.funds += 4.30
            self.specials += 1
            return payment 
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(2.5):
#            card.balance -= 2.50
            self.lunches += 1
            return True
        else:
            return False
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        

    def eat_special_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(4.3):
#            card.balance -= 4.30
            self.specials += 1
            return True
        else:
            return False
        
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        return card
    

