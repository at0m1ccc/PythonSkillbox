class SquaresIterator:
    def __init__(self, number):
        self.last_num = number
        self.current_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num <= self.last_num:
            result = self.current_num ** 2
            self.current_num += 1
            return result
        else:
            raise StopIteration


def gen_squares(last_num):
    current_num = 1
    while current_num <= last_num:
        yield current_num ** 2
        current_num += 1


number = int(input("Введите число N: "))

squares = (num ** 2 for num in range(1, number + 1))

print('Генераторное выражение:')
for square_num in squares:
    print(f'Квадрат числа = {square_num}')
print()

print('Функция-генератор:')
for square_num in gen_squares(number):
    print(f'Квадрат числа = {square_num}')
print()

print('Класс-итератор:')
for square_num in SquaresIterator(number):
    print(f'Квадрат числа = {square_num}')
