class BankAccount:
    def __init__(self,account_balance=0):
        self.__account_balance = account_balance
    def deposit(self,amount):
        # In this case the return statement is absent because it is not important in deposit
        # Encapsulation is employed in the account_balance attribute to make it private protecting data integrity
       self.__account_balance +=  amount
    def withdraw(self,amount):
        if amount <= self.account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f'Your account balance is {self.__account_balance}')
        
# BankAccount(300)
# BankAccount.deposit(200)
my_account = BankAccount()
my_account.deposit(200)
my_account.display_balance()

