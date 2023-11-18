print('Задача 5. Маятник ')


def count_fluctuations(start, end):
    count_fluct = 0
    while start > end:
        count_fluct += 1
        start *= 0.916
    return count_fluct


def main():
    start_amplitude = float(input('Введите начальную амплитуду: '))
    end_amplitude = float(input('Введите амплитуду остановки: '))
    print(f'Маятник считается остановившимся через {count_fluctuations(start_amplitude, end_amplitude)} колебаний')


main()
