import re
import examples

urls = examples.urls

pattern = re.compile(r'https?://(www\.)?(\w+)(\w+)')
matchers = pattern.finditer(urls)

for el in matchers:
    print(el.group())

matchers = pattern.finditer(urls)
subbed_str = re.sub(r'https?://(www\.)?(\w+)(\w+)', r'\2\3', urls)
print(subbed_str)

