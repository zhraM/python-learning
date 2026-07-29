#practice1
file = open("text.txt","w")
file.write("Hello Python")
file.close()

#practice2
file = open("text.txt","r")
print(file.read())
file.close()

#practice3
file = open("text.txt","a")
file.write("\nLearning Files")
file.close()

#practice4
file = open("text.txt","r")
for line in file:
    print(line,end="")
file.close()

#practice5
names = open("names.txt","a")
name = input("Enter name: ")
names.write(name)
names.close()

#mini_project
users = open("users.txt","a")
name = input("Enter your name: ")
age = input("Enter your age: ")
users.write(name)
users.write(" - ")
users.write(age + "\n")
users.close()

users = open("users.txt","r")
print(users.read())
users.close()