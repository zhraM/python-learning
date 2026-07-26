#practice1
person = {
    "name" : "Shokat",
    "age" : 52,
    "city" : "Gonabad"
}
print(person)

#practice2
print(person["age"])

#practice3
person["age"] = 3

#practice4
person["job"] = "Mother"

#practice5
del person["city"]

#practice6
print("age" in person)

#practice7
print(person.items())

#practice8
name = input("Enter name: ")
age = int(input("Enter age: "))
user_info = {
    "name" : name,
    "age" : age
}
print(user_info)

#practice9
lesson = []
score = []
for i in range(5):
    lesson.append(input("Enter lesson: "))
    score.append(int(input("Enter score: ")))
report_card = {
    lesson[0] : score[0],
    lesson[1] : score[1],
    lesson[2] : score[2],
    lesson[3] : score[3],
    lesson[4] : score[4]
}
print(report_card)