course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

try:
    key = input("Please enter a key: ")
    value = course[key]
    print(f"Value for key '{key}': {value}")
except KeyError:
    print(f"The key '{key}' not found in dictionary 'course'.")
except Exception as e:
    print(f"Error: {e}")
