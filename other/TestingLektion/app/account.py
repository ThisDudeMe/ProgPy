class InsufficentAmount(Exception):
    pass

class Account:
    
    def __init__(self, initial_amount) -> None:
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficentAmount
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount