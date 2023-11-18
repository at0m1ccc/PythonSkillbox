import json
import requests

response = requests.get('https://swapi.dev/api/starships/')

data_millennium_falcon = next((ship for ship in response.json()['results']
                               if ship['name'] == 'Millennium Falcon'), None)
info_pilots = list()
for pilot in data_millennium_falcon['pilots']:
    pilot_data = requests.get(pilot).json()
    info_pilot = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': requests.get(pilot_data['homeworld']).json()['name'],
        'homeworld_url': requests.get(pilot_data['homeworld']).json()['url']
    }
    info_pilots.append(info_pilot)

millennium_falcon = {
    'ship_name': data_millennium_falcon['name'],
    'starship_class': data_millennium_falcon['starship_class'],
    'max_atmosphering_speed': data_millennium_falcon['max_atmosphering_speed'],
    'pilots': info_pilots
}

print(millennium_falcon)

with open('data_millennium_falcon.json', 'w') as file:
    json.dump(millennium_falcon, file, indent=4)
