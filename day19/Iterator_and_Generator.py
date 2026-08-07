#practice1
def count():
    yield from range(1, 11)
for num in count():
    print(num)

#practice2
def odd_numbers():
    for i in range(1, 20):
        if i % 2 == 1:
            yield i
for num in odd_numbers():
    print(num)
    
#practice3
def square_numbers(n):
    for i in range(n):
        yield i * i
for num in square_numbers(5):
    print(num)

#practice4
def fibonacci(n):
   x = 0
   y = 1
   for i in range(n):
       yield x
       x, y = y, x + y
for num in fibonacci(10):
    print(num)