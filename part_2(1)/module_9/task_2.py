import os


def print_reverse_file(file_name):
    zen = open(file_name, 'r')
    list_zen = []
    for i in enumerate(zen):
        list_zen.append(i[1])
    zen.close()
    list_zen[-1] += '\n'
    list_zen.reverse()
    print(''.join(list_zen))


print_reverse_file('zen.txt')
