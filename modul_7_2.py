
info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='UTF-8')
    string_positions = {}
    for n in strings:
        b = file.tell()
        file.write(f'{n}\n')
        c = strings.index(n)+1
        coordinates = (b,c)
        string_positions[coordinates ] = n
    file.close()
    # print(string_positions)
    return string_positions

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)