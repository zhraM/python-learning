#practice1
count = 1
while count <= 10 :
    print(count)
    count += 1
    
#practice2
n = int(input("Enter number: "))
s = 0
while n >= 1 :
    s += n
    n -= 1
print(s)

#practice3
n = int(input("Enter number: "))
while n!= 0 :
    n = int(input("Enter number: "))
print("Program Ended")

#practice4
num = int(input("Enter number: "))
fact = 1
while num >= 1 :
    fact *= num
    num -= 1
print(fact)

#practice5
password = ""
while password != "python-day04" :
    password = input("Enter password: ")
print("Access Granted")