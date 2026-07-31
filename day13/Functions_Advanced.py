#practice
def find_max(*numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
    
#mini_project
def add(a ,b):
    return a + b
def sub(a ,b):
    return a - b
def mul(a ,b):
    return a * b
def divide(a ,b):
    return a / b
try:
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    c = input("Enter operator: ")
    if c == '+':
        print(add(a ,b))
    elif c == '-':
        print(sub(a ,b))
    elif c == '*':
        print(mul(a ,b))
    elif c == '/':
        if b == 0:
            print("Zero Division Error")
        else:
            print(divide(a ,b))
    else:
        print("Invalid Operator")
except ValueError:
    print("Enter numbers")