import random

start_list = [random.randint(0, 1000) for _ in range(10)]
print(f'Оригинальный список: {start_list}')
print(f'Новый список(1 способ): '
      f'{[(start_list[num * 2], start_list[num * 2 + 1]) for num in range(0, len(start_list) // 2)]}')
print(f'Новый список(2 способ): {list(zip(start_list[::2], start_list[1::2]))}')
