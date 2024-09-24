mport time

directory = 'C:\PythonJobs\Module_7'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, путь: {filepath}, размер: {filesize} байт, время размещения: {formatted_time}, '
              f'родительская директория: {parent_dir}')
    break
