from random import randint
from text import *


class Account:
    def __init__(self, account_id: int, password: int):
        self.accountId = account_id
        self.balance = 0
        self.password = password
        self.number = list(randint(0, 9) for _ in range(16))

    def add_balance(self, sum: int):
        if self.check_pass():
            self.balance += sum
            print(mission_complete)
        else:
            print(password_error)

    def withdraw_money(self, sum: int):
        if self.check_pass():
            if sum > self.balance:
                print(balance_error)
            else:
                self.balance -= sum
                print(mission_complete)
                return sum  # Типа налик вернул)
        else:
            print(password_error)

    def check_pass(self) -> bool:
        password = input(check_password)
        if password.isdigit():
            password = int(password)
            if password == self.password:
                return True
            else:
                return False
        else:
            return False