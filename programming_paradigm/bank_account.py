class BankAccout:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            # The statement measures if the withdrawal was a success
            return True
        else:
            # This statement measures if the withdrawal was a fail.
            return False

    def display_balance(self):
        print(f'The current account balance is {self.account_balance}')
