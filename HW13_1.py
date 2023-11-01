import re
import examples

text_to_search = examples.text_to_search

pattern = re.compile(r'abc', re.IGNORECASE)
matchers = pattern.finditer(text_to_search)

for match in matchers:
    print(match)








