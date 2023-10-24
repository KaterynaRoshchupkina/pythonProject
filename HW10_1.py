def arithmetic_operation(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Division by zero is not allowed"
        else:
            return a / b
    else:
        return f'Not known operation: {operation}'

# Example usage:
result = arithmetic_operation(5, 3, '+')
print(result)

result = arithmetic_operation(10, 2, '-')
print(result)

result = arithmetic_operation(6, 4, '*')
print(result)

result = arithmetic_operation(8, 2, '/')
print(result)

result = arithmetic_operation(7, 0, '/')
print(result)

result = arithmetic_operation(7, 3, '^')
print(result)


