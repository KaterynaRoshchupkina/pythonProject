def print_function_name(func):
    def wrapper(*args, **kwargs):
        print('Function Name:', func.__name__)
        return func(*args, **kwargs)

    return wrapper


def custom_max(iterable):
    if not iterable:
        raise ValueError('max() arg is an empty sequence')

    max_value = iterable[0]
    for item in iterable:
        if item > max_value:
            max_value = item
    return max_value

def custom_min(iterable):
    if not iterable:
        raise ValueError('min() arg is an empty sequence')

    min_value = iterable[0]
    for item in iterable:
        if item < min_value:
            min_value = item
    return min_value


numbers = [3, 1, 7, 4, 2, 9]
maximum = custom_max(numbers)
minimum = custom_min(numbers)
