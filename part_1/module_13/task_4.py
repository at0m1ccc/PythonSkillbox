print('Задача 4. Недоделка 2')


def count_numbers(number):
    num_count = 0
    while number > 0:
        num_count += 1
        number = number // 10
    return num_count


def change_number(number, num_count):
    last_digit = number % 10
    first_digit = number // 10 ** (num_count - 1)
    between_digits = number % 10 ** (num_count - 1) // 10
    return last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit


def main():
    first_n = int(input("Введите первое число: "))
    if count_numbers(first_n) < 3:
        print("В первом числе меньше трёх цифр.")
    else:
        first_n = change_number(first_n, count_numbers(first_n))
        print('Изменённое первое число:', first_n)
    second_n = int(input("\nВведите второе число: "))
    if count_numbers(second_n) < 4:
        print("Во втором числе меньше четырёх цифр.")
    else:
        second_n = change_number(second_n, count_numbers(second_n))
        print('Изменённое второе число:', second_n)
    print('\nСумма чисел:', first_n + second_n)


main()
