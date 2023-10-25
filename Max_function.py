def custom_max(iterable):
    if not iterable:
        raise ValueError("max() arg is an empty sequence")

    max_value = iterable[0]
    for item in iterable:
        if item > max_value:
            max_value = item
    return max_value


# Example usage:
numbers = [3, 1, 7, 4, 2, 9]
maximum = custom_max(numbers)
print('Maximum value:', maximum)
