#practice1
class Book:
    def __init__(self ,title , author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def info(self):
        print(self.title)
        print(self.author)
        print(self.pages)
b = Book("beeing", "alireza", 1348)
b.info()

#practice2
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance -= amount
    def show_balance(self):
        print(self.balance)

ba = BankAccount("ali", 1000)
ba.deposit(600)
ba.withdraw(750)
ba.show_balance()

#practice3
class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = list(grades)
    def add_grade (self, score):
        self.grades.append(score)
    def average(self):
        s=0
        for grade in self.grades:
            s += grade
        print("average = ", s/len(self.grades))
    def show(self):
        print(self.name , ":")
        for grade in self.grades:
            print(grade)
a = Student("ali",18, 20, 17)
a.show()
a.average()

#practice4
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def is_square(self):
        print(self.length == self.width)
    def perimeter(self):
        print(2 * (self.length + self.width))
    def area(self):
        print(self.length * self.width)
r = Rectangle(2 ,4)
r.area()
r.is_square()
r.perimeter()

#practice5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase(self, percent):
        self.salary += percent * self.salary / 100
e = Employee("zhra",1000000)
e.increase(25)
print(e.salary)

#practice6
class ShoppingCart:
    def __init__(self, *items):
        self.items = list(items)
    def add(self, item):
        self.items.append(item)
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found")
    def show_items(self):
        for item in self.items:
             print(item)
    def count(self):
        print(len(self.items))
sc = ShoppingCart("sherkat", "Gold", "Silver", "Horse")
sc.add("Dimond")
sc.remove("Bronze")
sc.remove("Horse")
sc.show_items()
sc.count()

#practice7
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def accelerate(self):
        self.speed += 10
    def brake(self):
        if self.speed > 10:
            self.speed -= 10
        else:
            self.speed = 0
    def show_speed(self):
        print(self.speed)
c = Car("lamborghini",6)
c.brake()
c.accelerate()
c.brake()
c.show_speed()

#practice8
class Library:
    def __init__(self, *books):
        self.books = list(books)
    def add_book(self, item):
        self.books.append(item)
    def remove_book(self, item):
        self.books.remove(item)
    def search(self, item):
        for book in self.books:
            if book == item:
                return True
        return False
    def show_books(self):
        for book in self.books:
            print(book)

b = Library("night", "day", "sun", "moon", "programming")
b.add_book("rain")
b.remove_book("programming")
print(b.search("cloud"))
b.show_books()

#practice9
class UniStudent:
    def __init__(self, name, age, average):
         self.name = name
         self.age = age
         self.average =average
class ManageStudents:
    def __init__(self, *UniStudent):
        self.UniStudent = list(UniStudent)
    def add_student(self, student):
        self.UniStudent.append(student)
    def remove_student(self, student):
        self.UniStudent.remove(student)
    def show_students(self):
        for student in self.UniStudent:
            print(student.name,
                  student.age,
                  student.average)
    def best_student(self):
        best = self.UniStudent[0]
        for student in self.UniStudent:
            if student.average > best.average :
                best = student
        print(best.name)
s1 = UniStudent("shokat", 52, 20)
s2 = UniStudent("alireza", 57, 19.9)
s3 = UniStudent("zhra", 24, 17)
us = ManageStudents(s1, s2, s3)
us.add_student(UniStudent("ali", 2, 19))
us.best_student()
us.show_students()

#mini_project
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def attack(self, enemy):
        if enemy.health > 10:
            enemy.health -= 10
        else:
            enemy.health = 0
            print("Game Over")
            
    def heal(self):
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
    def status(self):
        print(self.health)

p1 = Player("shokat")
p2 = Player("alireza")

p1.attack(p2)
p2.attack(p1)
p1.attack(p2)
p2.heal()
p1.status()
p2.status()