import json
#practice1
user = {
    "name":"shokooh",
    "age": 52,
    "city":  "gonabad",
    "skills": "cute"
}
data = json.dumps(user)
print(data)
print(type(data))

#practice2
data = '{"name": "shokooh", "age": 52, "city": "gonabad"}'
user = json.loads(data)
print(user)
print(type(user))

#practice3
with open("user.json", "w") as file:
    json.dump(user, file)

#practice4
users = [
    {"name": "Ali", "age": 25, "city": "Tehran"},
    {"name": "Sara", "age": 30, "city": "Shiraz"},
    {"name": "Reza", "age": 22, "city": "Mashhad"}
]
with open("users.json", "w") as file:
    json.dump(users, file)
    
#practice5
with open("users.json", "r") as file:
    users = json.load(file)
print(users)
print(type(users))
print(users[0]["name"])

#practice6
for user in users:
    print(user["name"])
    
#practice7
user = {
    "name": "Shokooh",
    "age": 52,
    "city": "Gonabad"
}
with open("users_data.json", "w") as file:
    json.dump(user, file)
with open("users_data.json", "r") as file:
    print(json.load(file))

#practice8
user = {
    "name": "Shokooh",
    "age": 52,
    "address": {
        "city": "Gonabad",
        "country": "Iran"
    }
}
with open("user_info.json", "w") as file:
    json.dump(user, file)
with open("user_info.json", "r") as file:
    print(json.load(file))
print(user["address"]["city"])

#practice9
with open("user_info.json", "r") as file:
    data = json.load(file)
data["age"] = 53
data["address"]["city"] = "Mashhad"
with open("user_info.json", "w") as file:
    json.dump(data, file)
with open("user_info.json", "r") as file:
    data = json.load(file)
print(data)