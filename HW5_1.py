divisor = int(input('Please enter the number to divide:'))
numbers = [10, 12, 20, 36, 60, 88]
result = []

for number in numbers:
    if number % divisor == 0:
        result.append(number)

print('Numbers that are divisible by', 'divisor', 'are:', 'result')

