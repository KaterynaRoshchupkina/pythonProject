lst_1 = [1, 2, 3, 4, 5, 6, 7]
lst_2 = [4, 5, 6, 7, 8, 9, 10]

my_set_1 = set(lst_1)
my_set_2 = set(lst_2)

elements_not_in_lst_2 = my_set_1 - my_set_2

result = list(elements_not_in_lst_2)

print(result)
