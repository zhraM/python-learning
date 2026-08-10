#practice1
square = [ i ** 2 for i in range(1,11)]
print(square)

#practice2
numbers = [12, 5, 8, 21, 30, 7, 44, 9]
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)

#practice3
numbers = [1, 2, 3, 4, 5]
times_ten = [x * 10 for x in numbers]
print(times_ten)

#practice4
words = ["python", "java", "c++", "javascript", "go"]
long_words = [word for word in words if len(word) > 3]
print(long_words)

#practice5
numbers = [1, 2, 3, 4, 5]
squares = {x: x ** 2 for x in numbers}
print(squares)

#practice6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_square = {i: i ** 2 for i in numbers if i % 2 == 0}
print(even_numbers_square)

#practice7
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
square = {x ** 2 for x in numbers}
print(square)

#practice8
numbers = [1, 2, 3]
multiply = [x * y for x in numbers for y in range(1, 4)]
print(multiply)

#practice9
words = ["python", "java", "c++", "go", "javascript"]
lengths = [len(word) for word in words]
print(lengths)