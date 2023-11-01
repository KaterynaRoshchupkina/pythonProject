import re

pattern = re.compile(r'\b[\w.-]+@[\w.-]+\.\w+\b')

with open('data.txt', 'r') as file:
    content = file.read()
matchers = pattern.findall(content)
print(matchers)
