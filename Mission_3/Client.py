from Account import Account
from text import *


class Client:

    def __init__(self, name: str, surname: str, client_id: int):
        self.name = name
        self.surname = surname
        self.client_id = client_id
        self.accounts = list()

    def open_account(self, id_account: int, password: str):
        if password.isdigit():
            new_account = Account(id_account, int(password))
            self.accounts.append(new_account)
            print(mission_complete)
        else:
            print(password_error)

    def close_account(self, account_num):
        if self.accounts[account_num].check_pass():
            self.accounts.pop(account_num)
        else:
            print(password_error)
