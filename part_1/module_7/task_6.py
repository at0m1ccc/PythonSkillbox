print('Задача 6. Замечательные числа')
print('Двузначные числа, равные утроенному произведению своих цифр:')
for number in range(10, 100):
    if (number // 10) * (number % 10) * 3 == number:
        print(number)
