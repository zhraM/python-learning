#practice1 
name = "Zahra"
print(name)

#practice2
print(name[0])
print(name[4])

#practice3
print(len(name))

#practice4
for char in name:
    print(char)
    
#practice5
text = input("Enter text: ")
print('a' in text)

#practice6
name = input("Enter your name: ")
print("Hello "+ name)

#practice7
print(name * 5)

#practice8
print(text.upper())

#practice9
print(text.strip())

#practice10
sentence = "I love java"
print(sentence.replace("java","python"))

#practice11
print(text.count('a'))

#practice12
count = 0
for char in text:
    if char != " ":
        count +=1
print("Character numbers: ",count)
print("First character: ",text[0])
print("Last character: ",text[-1])
print(text.upper())
print(text.lower())

#mimi_project
vowels = 0
for char in text.lower():
    if char == "a" or char == "o" or char == "u" or char == "i" or char == "e":
        vowels += 1
print("Vowels: ",vowels)