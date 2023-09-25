s = input("Please enter a string: ")
s = s.lower()
n = 'palindrome'


if str(s) == str(s)[::-1]:
    print(f"String is a {n}")
else:
    print(f"String is not a {n}")