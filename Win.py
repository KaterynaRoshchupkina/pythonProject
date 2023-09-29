lst = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
inner_list = lst[-1]
nested_list = inner_list[-1]
win_value = nested_list[-1]
new_list = [win_value]
print(new_list)