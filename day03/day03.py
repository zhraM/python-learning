#practice1
number = int(input("Enter a number: "))
if number % 2 == 0 :
    print("Even")
else:
    print("Odd")
    
#practice2
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
if a >= b and a >= c :
    print("Largest:", a)
elif b >= a and b >= c :
    print("Largest:", b)
else :
    print("Largest:", c)

#practice3
score = int(input("Enter your score: "))   
if score > 18 :
    print("Excellent")
elif score <=18 and score >=12 :
    print("Passed")
else :
    print("Failed")

#practice4
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Teenager")
elif 18 <= age <= 60:
    print("Adult")
else:
    print("Senior")