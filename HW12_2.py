def square_even_numbers():
    squares = [x**2 for x in range(0, 1000000001, 2)]
    return squares


result = square_even_numbers()

print(result[:10])
