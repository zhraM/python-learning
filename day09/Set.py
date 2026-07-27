#practice4
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)

#practice5
numbers.add(10)
print(numbers)

#practice6
numbers.remove(3)
print(numbers)

#practice7
num = int(input("Enter number: "))
if num in numbers:
    print("Exists")
else:
    print("Not exists")
    
#practice8
numbers = set()
for i in range(5):
    num = int(input("Number: "))
    numbers.add(num)
print(len(numbers))