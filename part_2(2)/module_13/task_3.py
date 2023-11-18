import os


def gen_count_lines_python_files(directory='C:/'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                path_to_file = os.path.join(root, file)
                with open(path_to_file, 'r') as py_file:
                    lines = py_file.readlines()
                    not_empty_lines_list = [line for line in lines if line.strip() and not line.strip().startswith('#')]
                    yield path_to_file, len(not_empty_lines_list)


for path_to_file, count_not_empty_lines in gen_count_lines_python_files('C:/Users'):
    print(f'В файле {path_to_file}: {count_not_empty_lines} не пустых и не закомментированных строчек!')
