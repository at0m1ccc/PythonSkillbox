def print_nums(num):
    if num != 1:
        print_nums(num - 1)
    print(num)


number = int(input('Введите num: '))
print_nums(number)
