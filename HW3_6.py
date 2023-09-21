currency_1 = 'UAH'
currency_2 = 'USD'
currency_3 = 'EUR'
n = 0.027
n1 = 36.56
m = 0.025
m1 = 38.87
operation_1 = input('Please enter the amount in UAH to convert to USD:')
print(int(operation_1) * float(n))
operation_2 = input(f'Please enter the amount in {currency_2} to convert to {currency_1}:')
print(int(operation_2) * float(n1))
operation_3 = input(f'Please enter the amount in {currency_1} to convert to {currency_3}:')
print(int(operation_3) * float(m))
operation_4 = input(f'Please enter the amount in {currency_3} to conver to {currency_1}:')
print(int(operation_3) * float(m1))