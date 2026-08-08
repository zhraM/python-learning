#practice1
def decorator(func):
    def wrapper():
        print ("Start")
        func()
        print("End")
    return wrapper
@decorator
def login():
    print("User logged in")
login()

#practice2
def count(func):
    i = 1
    def wrapper():
        nonlocal i
        func()
        print(f"Executed {i} times")
        i += 1
    return wrapper
@count
def hello():
    print("Hi")
hello()
hello()
hello()

#practice3
def log(func):
    def wrapper(a, b):
        print("Function add started")
        print(f"Result: {func(a, b)}")
        print("Function add finished")
    return wrapper
@log
def add(a, b):
    return a + b
add(3, 4)

#practice4
def check_positive(func):
    def wrapper(n):
        if n < 0:
            print("Number must be positive")
        else:
            print(func(n))
    return wrapper
@check_positive
def square(n):
    return n * n
square(3)
square(-4)