from random import randint


class Unit:
    def __init__(self, name='Воин', health=100, damage=20):
        self.name = name
        self.health = health
        self.damage = damage

    def static_health(self):
        print(f'У {self.name} осталось {self.health} здоровья\n')


def battle(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        if randint(0, 1) == 0:
            unit_2.health -= unit_1.damage
            print(f'{unit_1.name} атаковал {unit_2.name}')
            unit_2.static_health()
        else:
            unit_1.health -= unit_2.damage
            print(f'{unit_2.name} атаковал {unit_1.name}')
            unit_1.static_health()
    if unit_1.health != 0:
        print(f'Победил {unit_1.name}')
    else:
        print(f'Победил {unit_2.name}')


battle(Unit(name='Воин 1'), Unit(name='Воин 2'))
