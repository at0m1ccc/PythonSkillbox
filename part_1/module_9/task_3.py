print('Задача 3. Театр')
rows_count = int(input('Введите кол-во рядов: '))
seat_in_row_count = int(input('Введите кол-во сидений в ряде: '))
meters_between_rows = int(input('введите кол-во метров между рядами: '))

print('\nСцена', end='\n' * 2)
for row in range(rows_count):
    print('=' * seat_in_row_count + ' ' + '*' * meters_between_rows + ' ' + '=' * seat_in_row_count)
