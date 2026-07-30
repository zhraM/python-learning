#practice1
try:
    num = int(input("Enter number: "))
except:
    print("Not a number!")
    
#practice2
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except:
    print("Erorr!")

#practice3
file = input("Enter file's name: ")
try:
    open(file + ".txt")
except:
    print("File not found.")

#practice4
try:
    num = int(input("Number: "))
    print(100 / num)
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")

#mini_project
try:
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    c = input("Enter operator: ")
    print(a,c,b , "=")
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
    else:
        print("Invalid Operator")
    
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero Division Error")