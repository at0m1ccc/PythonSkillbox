import os


def find_size_dirs_files(file_name):
    files = 0
    dirs = 0
    dir_size = 0
    for dirway, dirnames, filenames in os.walk(file_name):
        for f_name in filenames:
            dir_size += os.path.getsize(os.path.join(dirway, f_name))
        files += len(filenames)
        dirs += len(dirnames)
    dir_size /= 1024
    return dir_size, dirs, files


path_to_dir_name = os.path.abspath(os.path.join('..', '..', input('Введите путь до каталога: ')))
if os.path.exists(path_to_dir_name):
    result = find_size_dirs_files(path_to_dir_name)
    print(f'Размер каталога (в Кбайтах): {result[0]}')
    print(f'Количество подкаталогов: {result[1]}')
    print(f'Количество файлов: {result[2]}')
else:
    print('Такого каталога нет на компьютере!')
