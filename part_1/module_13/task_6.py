print('Задача 6. Яйца')


def danger_lvl_formula(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10


def find_optimal_depth(max_danger_lvl):
    min_depth = 0
    max_depth = 4
    average = (max_depth + min_depth) / 2
    while abs(danger_lvl_formula(average)) > max_danger_lvl:
        if abs(danger_lvl_formula(min_depth)) > abs(danger_lvl_formula(max_depth)):
            min_depth = average
        else:
            max_depth = average
        average = (max_depth + min_depth) / 2
    return average


def main():
    max_danger_lvl = float(input('Введите максимально допустимый уровень опасности: '))
    result = find_optimal_depth(max_danger_lvl)
    print(f'Приблизительная глубина безопасной кладки: {result} м')


main()
