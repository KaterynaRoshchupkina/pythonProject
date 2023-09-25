lst = [1, 6, 4, 8, 12]
is_sorted = lst == sorted(lst)
l = 'list'
if is_sorted:
    print(f'The {l} is sorted correctly')
else:
    print(f'The {l} is not sorted correctly')