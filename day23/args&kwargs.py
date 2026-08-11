#practice1
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_numbers(10, 20, 30, 40))

#practice2
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
show_info(name="Yasi", age=22, city="ahvaz")

#practice3
def calculate(*args, **kwargs):
    if kwargs["operation"] == "sum":
        total = 0
        for num in args:
            total += num
        return total
    if kwargs["operation"] == "max":
        return max(args)
print(calculate(10, 20, 5, name="Yasi", operation="sum"))

#practice4
def calculate_average(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)
print(calculate_average(10, 20, 30, 40))

#practice5
def find_student(**kwargs):
    best = max(kwargs.values())
    for key, value in kwargs.items():
        if best == value:
            return key
print(find_student(Yasi=18, Sara=20, Mina=17))

#practice6
def combine_data(*args, **kwargs):
    total = 0
    for num in args:
        total += num
    kwargs["total"] = total
    print(kwargs)
combine_data(10, 20, 30, name="Yasi", age=22)

#practice7
def filter_kwargs(**kwargs):
    new_kwargs = {}
    for key, value in kwargs.items():
        if type(value) == int:
            if value > 10:
                new_kwargs[key] = value
    print(new_kwargs)
filter_kwargs(age=22, score=8, height=160, name="Yasi")

#practice8
def calculate(*args, **kwargs):
    if kwargs["operation"] == "sum":
        return sum(args)
    if kwargs["operation"] == "average":
        return sum(args) / len(args)
    if kwargs["operation"] == "max":
        return max(args)
    return "Invalid operation"
print(calculate(10, 20, 30, operation="average"))

#practice9
def analyze_numbers(*args):
    numbers = {
        "positive": 0,
        "negative": 0,
        "zero": 0
    }
    for i in args:
        if i == 0 :
            numbers["zero"] += 1
        elif i < 0:
            numbers["negative"] += 1
        else:
            numbers["positive"] += 1
    return numbers
print(analyze_numbers(10, -5, 0, 7, -2, 0))