import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, путь: {filepath}, размер: {filesize} байт, время размещения: {formatted_time}, '
              f'родительская директория: {parent_dir}')