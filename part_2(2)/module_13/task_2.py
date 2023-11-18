import os


def generation_path_to_file(directory='C:/'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


for path_to_file in generation_path_to_file('C:/Users'):
    print(path_to_file)
