print('Задача 3. Поступление')
place_in_list = int(input('Введите место в списке поступающих: '))
if place_in_list > 10:
    print('К сожалению, вы не поступили.')
else:
    scores_count = int(input('Введите количество баллов за экзамены: '))
    print('Поздравляем, вы поступили!')
    if scores_count >= 290:
        print('Бонусом вам будет начисляться стипендия.')
    else:
        print('Но вам не хватило баллов для стипендии.')
