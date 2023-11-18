print('Задача 5. Обычный день на работе')
print('Начался восьмичасовой рабочий день.')
hour = 1
sum_task = 0
wife_call_flag = 0
while hour <= 8:
    print(f'{hour}-й час')
    sum_task += int(input('Сколько задач решит Максим? '))
    wife_call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if wife_call == 1 and wife_call_flag != 1:
        wife_call_flag = 1
    hour += 1
print('Рабочий день закончился. Всего выполнено задач:', sum_task)
if wife_call_flag == 1:
    print('Нужно зайти в магазин.')
