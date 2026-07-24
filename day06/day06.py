#practice1
def welcome():
    print("Welcome")
    
welcome()

#practice2
def hello(name):
    print("Hello", name)
    
name = input("Enter your name: ")
hello(name)

#practice3
def add(a,b):
    print(a + b)
    
a = int(input())
b = int(input())
add(a , b)

#practice4
def add_numbers(a , b):
    return a + b

s = add_numbers(a , b)
print(s)
    
#practice5
def identify(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
identify(int(input("Enter number: ")))

#practice6
def is_prime(num):
    prime = True
    if num == 1 :
        return False
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
    return prime

#practice7
def sum_numbers(number):
    s = 0
    while number >= 1:
        s += number
        number -= 1
    return s

print(sum_numbers(int(input("Enter number: "))))