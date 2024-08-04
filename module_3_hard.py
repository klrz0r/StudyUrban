def calculate_structure_sum(*args):
    count = 0
    for i in args:
        if isinstance(i, str):
            count = count + len(i)
        elif isinstance(i, int):
            count = count + i
        elif isinstance(i, dict):
            count = count + calculate_structure_sum(i.items())
        else:
            count = count + calculate_structure_sum(*i)
    return int(count)


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)