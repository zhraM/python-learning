#practice1
cube = lambda x: x ** 3
print(cube(3))

#practice2
maximum = lambda a, b: a if a > b else  b
print(maximum(10, 7))

#practice3
check = lambda y: "Positive" if y > 0 else "Negative" if y < 0 else "Zero"
print(check(5))
print(check(-3))

#practice4
square = lambda a: a ** 2
numbers = [1, 2, 3, 4, 5]
print(list(map(square, numbers)))

#practice5
discount = lambda x: int(0.9 * x)
prices = [100, 250, 80, 300, 150]
print(list(map(discount, prices)))

#practice6
make_upper = lambda x: x.upper()
users = ["Ali", "Sara", "Reza", "Mina", "John"]
print(list(map(make_upper, users)))

#practice7
scores = [12, 18, 7, 20, 9, 15, 4, 19]
accept = lambda a: a >= 10
print(list(filter(accept, scores)))

#practice8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = lambda b: b%2 == 0
print(list(map(square, filter(even_numbers, numbers))))

#practice9
names = ["ali", "sara", "mohammad", "reza", "mina", "hossein"]
long_names = lambda a: len(a) > 4
print(list(filter(long_names, names)))

#practice10
from functools import reduce
numbers = [2, 3, 4, 5]
print(reduce(lambda a, b: a * b, numbers))

#practice11
numbers = [10, 20, 30, 40, 50]
sum_numbers = lambda a, b: a + b
print(reduce(sum_numbers, numbers))

#practice12
numbers = [12, 45, 7, 89, 23, 56]
print(reduce(maximum, numbers))

#practice13
numbers = [34, 12, 67, 5, 89, 23, 8]
minimum = lambda a, b: a if a < b else b
print(reduce(minimum, numbers))