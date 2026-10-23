class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума має бути більшою за нуль")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума має бути більшою за нуль")
        if amount > self.balance:
            return False

        self.balance -= amount
        return True