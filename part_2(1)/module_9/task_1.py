import os


def sum_number_in_file(file_name):
    with open(file_name, 'r') as file:
        num_sum = sum(int(num) for str_text in file for num in str_text.split())
    with open('answer.txt', 'w') as result_file:
        result_file.write(str(num_sum) + '\n')


sum_number_in_file('numbers.txt')
