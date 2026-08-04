#practice1
import square
print(square.area(7))
print(square.perimeter(6))

#practice2
from random import randint as r, choice
print(r(1, 100))

#practice3
a = []
for i in range(3):
    a.append(input("Enter name: "))
print(choice(a))

#practice4
import math
num = float(input("Enter a number: "))
print(math.sqrt(num))
print(math.factorial(int(num)))
print(math.ceil(num))
print(math.floor(num))