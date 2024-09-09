import io
import pprint

def custom_write(file_name, string):
    file = open(file_name, 'w', encoding='utf-8')
    string_position = {}
    for i in range(len(string)):
        bite_string = file.tell()
        numb_string = i + 1
        string_position[(numb_string, bite_string)] = string[i]
        file.write(f'{string[i]}\n')
    file.close()
    return string_position

info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

result = custom_write('Test.txt', info)
for elem in result.items():
    print(elem)

