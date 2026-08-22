#practice1
import re
text = "I love Python programming"
result = re.search("Python", text)
print(result)

#practice2
print(result.span())
print(result.group())

#practice3
text = "My phone number is 09123456789"
pattern = r"09\d{9}"
result = re.search(pattern, text)
print(result)

#practice4
text = "I am 23 years old"
result = re.search(r"\d", text)
print(result)
result1 = re.search(r"\d+", text)
print(result1)

#practice5
text = "My codes are 123 and 4567"
result = re.search(r"\d{3}", text)
print(result)

#practice6
text = "I have 3 cats and 12 dogs"
result = re.search(r"\d+", text)
print(result)

#practice7
text = "My password is abc123"
result = re.search(r"[a-z]{3}", text)
print(result)
result1 = re.search(r"pas[a-z]+", text)
print(result1)

#practice8
text = "I bought 3 apples, 5 bananas and 12 oranges"
result = re.findall(r"\d+", text)
print(result)

#practice9
text = "hello_123 world!"
result = re.findall(r"\w+", text)
print(result)
result1 = re.findall(r"\W", text)
print(result1)

#practice10
text = "I have 3 Cats, 12 Dogs and 5 birds"
result = re.findall(r"[a-zA-Z]+", text)
print(result)

#practice11
text = "My phone number is 09123456789"
result = re.sub(r"\d", "*", text)
print(result)

#practice12
text = "Python-Java-C++-JavaScript"
result = re.split(r"-", text)
print(result)

#practice13
text = "Python is awesome"
result = re.match(r"Python", text)
print(result)
result1 = re.match(r"awesome", text)
print(result1)

#practice14
text = "Python is my favorite language"
result = re.search(r"^Python", text)
print(result)
result1 = re.search(r"language$", text)
print(result1)

#practice15
text = "I have a cat"
result = re.search(r"[abc]", text)
print(result)
result1 = re.search(r"[^abc]", text)
print(result1)

#practice16
text = "I like Java"
result = re.search(r"(Python|Java)", text)
print(result)

#practice17
text = "I like color"
result = re.search(r"colou?r", text)
print(result)

#practice18
text = "ac"
result = re.search(r"ab*c", text)
print(result)

#practice19
text = "Contact me at ali123@gmail.com or sara99@yahoo.com"
result = re.findall(r"\w+@\w+\.com", text)
print(result)

#practice20
text = "Call me at 09121234567 or 09351234567"
result = re.findall(r"09\d{9}", text)
print(result)

#practice21
text = "Ali went to Tehran with Sara and Mohammad"
result = re.findall(r"[A-Z]\w+", text)
print(result)