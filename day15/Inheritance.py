#practice1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"my name is {self.name}")
        
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
s1 = Student("shokooh", 52, 20)
s1.introduce()
print(s1.grade)
    
#practice2
class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("Car is moving")
class Bike(Vehicle):
    def move(self):
        print("Bike is moving")
c = Car()
c.move()

#practice3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_info(self):
        print(f"{self.name}'s salary is: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
m1 = Manager("yoha", 48, "law")
m1.show_info()

#practice4
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal's sound")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Meowww")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Hop Hop")
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Maaaa")
animals = [
    Dog("Rocky"),
    Cat("Kitty"),
    Cow("Moo")
]
for animal in animals:
    animal.speak()
    
#practic5