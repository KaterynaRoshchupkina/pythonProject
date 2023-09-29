import lst

lst = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
u = 'upper'
l = 'lower'
lst.sort()
print(f'Sorted by {u} register:')
print(lst)
lst.sort(reverse = True)
print(f'Sorted by {l} register:')
print(lst)