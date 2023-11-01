import re
import examples

text_to_search = examples.text_to_search

pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
matchers = pattern.findall(text_to_search)
print(matchers)
