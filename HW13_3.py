import re

pattern = re.compile(r"\d{3}.\d{3}.\d{4}")

with open('data.txt', 'r') as file:
    content = file.read()
matchers = pattern.findall(content)
print(matchers)

