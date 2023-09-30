my_list = [1, 5, 6, 7, 68, 0, 10]
sorted_list = sorted(my_list)
first_non_consecutive = None
for i in range(1, len(sorted_list)):
    if sorted_list[i] != sorted_list[i -1] +1:
        first_non_consecutive = sorted_list[i]
        break

    if first_non_consecutive is None:
        print('All numbers in the list are consecutive')
    else:
        print(f'First non-consecutive number: {first_non_consecutive}')

