import random


def make_input_log(path_to_file, count_lines):
    lines = ['ERROR', 'OK', 'YES', 'NO', 'Hello']
    with open(path_to_file, 'w') as file:
        for _ in range(count_lines):
            file.write(f"{random.choice(lines)}\n")


def error_log_generator(path_to_file):
    with open(path_to_file, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line


def main():
    input_file_name = 'input.log'
    output_file_name = 'output.log'
    make_input_log(input_file_name, 1000)

    with open(output_file_name, 'w') as out_file:
        for error_line in error_log_generator(input_file_name):
            out_file.write(error_line)


main()
