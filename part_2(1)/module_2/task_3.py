count_video_card = int(input('Количество видеокарт: '))
list_video_cards = []
new_list_video_cards = []
max_video_card = 0

for num_video_card in range(count_video_card):
    video_card = int(input(f'Видеокарта {num_video_card + 1}: '))
    list_video_cards.append(video_card)
    if video_card > max_video_card:
        max_video_card = video_card

for card in list_video_cards:
    if card != max_video_card:
        new_list_video_cards.append(card)

print(f'\nСтарый список видеокарт: {list_video_cards}')
print(f'Новый список видеокарт: {new_list_video_cards}')
