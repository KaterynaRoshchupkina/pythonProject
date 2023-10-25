def custom_min(iterable):
    if not iterable:
        raise ValueError("min() arg is an empty sequence")

    min_value = iterable[0]
    for item in iterable:
        if item < min_value:
            min_value = item
    return min_value


# Example usage:
numbers = [3, 1, 7, 4, 2, 9]
minimum = custom_min(numbers)
print('Minimum value:', minimum)
