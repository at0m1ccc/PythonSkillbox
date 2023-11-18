import re


def check_correct_phone_numbers(numbers):
    for index, number in enumerate(numbers):
        if re.match(r'^[89]\d{9}$', number):
            print(f"{index + 1} номер: всё в порядке")
        else:
            print(f"{index + 1} номер: не подходит")


example_list = ['9999999999', '999999-999', '99999x9999']
check_correct_phone_numbers(example_list)
