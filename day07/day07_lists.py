#practice1
colors = ["red","blue","yellow"]
print(colors)

#practice2
numbers = [5, 10, 15, 20, 25]

print(numbers[2])

#practice3
numbers[0] = 100

#practice4
num = int(input("Enter a number: "))
numbers.append(num)
print(numbers)

#practice5
numbers = [10, 20 , 30, 40]
numbers.remove(20)
print(numbers)

#practice6
numbers = [9, 5, 2, 8, 1]
numbers.sort()
print(numbers)

#practice7
names = ["Shokat","Pooya","Alireza","Zahra"]
for i in names:
    print(i)
    
#practice8
numbers = [10, 20, 30, 40]
s = 0
for i in numbers:
    s += i
print(s)

#practice9
numbers = [12, 45, 7, 89, 23]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)

#practice10
numbers = [2, 5, 8, 11, 14, 17]
count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1
print(count)