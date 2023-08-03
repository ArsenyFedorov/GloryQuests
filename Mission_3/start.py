from text import *
from Account import Account
from Client import Client


class PrivateOffice:

    def __init__(self):
        print(start_work)
        self.__name = input(user_name)
        self.__surname = input(user_surname)
        self.client = Client(self.__name, self.__surname, 0)
        self.account_id = 0

    def start(self):
        while True:
            print(event_list)
            event = input(user_event)
            if not event.isdigit() or 0 > int(event) or 6 < int(event):
                print(event_error)
            else:
                match int(event):
                    case 1:
                        self.dell_account()
                    case 2:
                        self.add_account()
                    case 3:
                        self.wit_money()
                    case 4:
                        self.add_bal()
                    case 5:
                        self.print_money()
                    case 6:
                        break

    def dell_account(self):
        if len(self.client.accounts) == 0:
            print(dell_error)
        else:
            for i in range(len(self.client.accounts)):
                print(i + 1, f".{self.client.accounts[i].number}")
            del_number = input(dell_acc)
            if not del_number.isdigit() or 0 > int(del_number) or len(self.client.accounts) < int(del_number):
                print(event_error)
            else:
                self.client.close_account(int(del_number) - 1)
                print(mission_complete)

    def add_account(self):
        new_password = input(user_pass)
        new_password = new_password.replace(" ", "")
        if not new_password.isdigit():
            print(password_error)
        else:
            self.client.open_account(self.account_id, new_password)

    def add_bal(self):
        sum = input(coll_money)
        if sum.isdigit():
            if len(self.client.accounts) == 0:
                print(add_error)
            else:
                for i in range(len(self.client.accounts)):
                    print(i + 1, f".{self.client.accounts[i].number}")
                add_number = input(add_money)
                if not add_number.isdigit() or 0 > int(add_number) or len(self.client.accounts) < int(add_number):
                    print(event_error)
                else:
                    self.client.accounts[int(add_number) - 1].add_balance(int(sum))
                    print(mission_complete)
        else:
            print(type_error)

    def wit_money(self):
        sum = input(koll_money)
        if sum.isdigit():
            if len(self.client.accounts) == 0:
                print(wit_error)
            else:
                for i in range(len(self.client.accounts)):
                    print(i + 1, f".{self.client.accounts[i].number}")
                wit_number = input(wit_money)
                if not wit_number.isdigit() or 0 > int(wit_number) or len(self.client.accounts) < int(wit_number):
                    print(event_error)
                else:
                    print(mission_complete)
                    return self.client.accounts[int(wit_number) - 1].withdraw_money(int(sum))
        else:
            print(type_error)

    def print_money(self):
        if len(self.client.accounts) == 0:
            print(print_error)
        else:
            for i in range(len(self.client.accounts)):
                print(i + 1, f".{self.client.accounts[i].number}")
            sum_user = input(sum_money)
            if not sum_user.isdigit() or 0 > int(sum_user) or len(self.client.accounts) < int(sum_user):
                print(event_error)
            else:
                print(self.client.accounts[int(sum_user) - 1].balance)
                print(mission_complete)
