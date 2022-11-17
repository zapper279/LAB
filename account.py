class Account:
    def __init__(self, name: str) -> None:
        '''
        This method stores the account name and the beginning account balance
        :param name: The name of the account
        '''
        self.__account_name = name      #any name that suit your fancy
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        This method is used to add money to the account
        :param amount: The amount of money being deposited
        :return: True if the money can deposit, False if the money can't deposit
        '''
        if amount < 0 or amount == 0:
            return False          #any number less than 0 or 0 itself. The number can be a float or int
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True           #any number greater than 0. The number can be a float or int

    def withdraw(self, amount: float) -> bool:
        '''
        This method is used to remove money from the account
        :param amount: The amount of money being withdrawn
        :return: True if the money can withdraw, False if the money can't withdraw
        '''
        if amount < 0 or amount == 0 or amount > self.__account_balance:
            return False       #any negative numbers, 0, or any number greater than the balance. The number can be a float or int
        if amount > 0 and amount < self.__account_balance:
            self.__account_balance = self.__account_balance - amount
            return True        #any number that is greater than 0 and less than the balance. The number can be a float or int

    def get_balance(self):
        '''
        This method is used to get the account balance
        :return: the balance of the account
        '''
        return self.__account_balance

    def get_name(self):
        '''
        This method is used to get the account name
        :return: the name of the account
        '''
        return self.__account_name