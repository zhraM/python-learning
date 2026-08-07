#practice1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)
    def set_age(self, age):
        if(age >= 0):
            self.__age = age
        else:
            print("Invalid age")
    def get_age(self):
        return self.__age
s1 = Student("baran", 20)
s1.set_age(30)
s1.set_age(-5)
print(s1.get_age())

#practice2
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("balance is not enough")
            
#practice3 
    @property
    def balance(self):
        return self.__balance
account = BankAccount("Baran", 1000)
print(account.balance)

#practice4
class Employee:
    def __init__(self, name, income):
        self.name = name
        if income >= 0:
            self.__income = income
        else:
            self.__income = 0
            print("Invalid income")
    def increase(self, value):
        if value > 0:
            self.__income += value
    def info(self):
        print(f"name : {self.name}, income : {self.__income}")