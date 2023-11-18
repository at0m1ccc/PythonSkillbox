print('Задача 7. Пропавшая карточка')
count_cards = int(input('Введите количество карточек: '))
sum_all_card = 0
sum_without_lost_card = 0
for card in range(1, count_cards + 1):
    sum_all_card += card
for user_card in range(count_cards - 1):
    sum_without_lost_card += int(input('Введите номер оставшейся карточки: '))
print(f'Номер пропавшей карточки: {sum_all_card - sum_without_lost_card}')
