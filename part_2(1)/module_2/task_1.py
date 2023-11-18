result_list = []
end_number = int(input('Введите число: '))
for num in range(0, end_number // 2 + end_number % 2):
    result_list.append(num * 2 + 1)

print('Список из нечётных чисел от одного до N:', result_list)
