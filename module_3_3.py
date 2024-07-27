def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'Не строка', False]
print_params(*values_list)

values_dict = {'a': 5, 'b': 'Стркоа 3', 'c': [1, 2]}
print_params(**values_dict)

values_list_2 = [1, 'Error']
print_params(*values_list_2, 42)