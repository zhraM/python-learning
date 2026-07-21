#practice1
for i in range(1,11):
    print(i)

#practice2
for i in range(2,21,2):
    print(i)

#practice3
num = int(input("Enter number: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
    
#practice4
num = int(input("Enter number: "))
s=0
for i in range(1,num+1):
    s+=i
print(s)

#practice5
num = int(input("Enter number: "))
IsPrime=True
for i in range(2,num):
    if num % i == 0:
        IsPrime = False
        break
if IsPrime:
    print("Prime")
else:
    print("Not Prime")