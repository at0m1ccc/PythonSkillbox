def add_symmetries(list_nums):
    if list_nums == list_nums[::-1]:
        print('Последовательность симметрична. Ничего добавлять не надо.')
    else:
        copy_list_nums = list_nums.copy()
        count = 0
        while copy_list_nums != copy_list_nums[::-1]:
            count += 1
            copy_list_nums = list_nums.copy()
            for i in range(count):
                copy_list_nums.append(copy_list_nums[count - i - 1])
        print(f"Нужно приписать чисел: {count}")
        print(f"Сами числа: {copy_list_nums[-count:]}")


list_numbers = []
count_number = int(input('Количество чисел: '))
for _ in range(count_number):
    list_numbers.append(int(input('Число: ')))

print(f'Последовательность: {list_numbers}')
add_symmetries(list_numbers)
