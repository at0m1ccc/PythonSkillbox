import math


def find_sqrt_number(number):
    try:
        if number < 0:
            raise ValueError(f'Из числа {number} нельзя вычислить квадратный корень, так как это отрицательное число!')
        result = math.sqrt(number)
        print(f'Квадратный корень из числа {number} = {result}')
    except ValueError as exc:
        print(exc)
    except Exception as exc:
        print(type(exc))


find_sqrt_number(5)
find_sqrt_number(-10)
