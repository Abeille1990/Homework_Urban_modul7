
info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='UTF-8')
    for n in strings:
        b = file.tell()
        file.write(f'{n}\n')
        c = strings.index(n)+1
        print({f'({c},{b}):{n}'})
    file.close()


custom_write('test.txt', info)
