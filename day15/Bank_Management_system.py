#project
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Your balance is not enough")
    def show_balance(self):
        print(self.balance)
class SavingAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        return self.interest_rate * self.balance / 100
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, withdraw_limit):
        super().__init__(owner, balance)
        self.withdraw_limit = withdraw_limit
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print("Withdrawl limit exceeded")
        else:
            super().withdraw(self, amount)
class VIPAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
    def withdraw(self, amount):
        self.balance -= amount
    def show_balance(self):
        print(f"VIP account of {self.owner}\n balance = {self.balance}")

accounts = [
    SavingAccount("Ali", 1000, 10),
    CheckingAccount("Shokat", 2000, 500),
    VIPAccount("Zahra",3000)
]      
for account in accounts:
    account.show_balance() 
    account.withdraw(1381)
    account.deposit(50)
    account.show_balance()