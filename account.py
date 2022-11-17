class Account:
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        if amount < 0 or amount == 0:
            return False
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True

    def withdraw(self, amount: float) -> bool:
        if amount < 0 or amount == 0 or amount > self.__account_balance:
            return False
        if amount > 0:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
