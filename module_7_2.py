def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    count_string = 0
    dict_string = {}
    for string in strings:
        count_string += 1
        position = file.tell()
        id_string = (count_string, position)
        dict_string[id_string] = string
        file.write(f'{string}\n')
    file.close()
    return dict_string

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

