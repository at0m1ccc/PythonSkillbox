import re


text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

result_car = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', text)
result_taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b', text)

print(f'Список номеров частных автомобилей: {result_car}')
print(f'Список номеров такси: {result_taxi}')
