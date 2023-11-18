from random import randint


class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def __str__(self):
        return f'У {self.name} степень сытости {self.satiety}, а в доме: {self.house}'

    def eat(self):
        self.satiety += randint(5, 10)
        self.house.refrigerator_food -= randint(5, 10)
        print(f'{self.name} поел. Степень сытости {self.satiety}')

    def work(self):
        self.satiety -= randint(5, 10)
        self.house.nightstand_money += randint(5, 10)
        print(f'{self.name} работал, теперь его бюджет составляет: {self.house.nightstand_money}')

    def play(self):
        self.satiety -= randint(5, 10)
        print(f'{self.name} играл. Теперь степень его сытости: {self.satiety}')

    def shop(self):
        self.house.refrigerator_food += randint(5, 10)
        self.house.nightstand_money -= randint(5, 10)
        print(f'{self.name} сходил в магазин. Теперь кол-во еды: {self.house.refrigerator_food}, ' 
              f'а бюджет: {self.house.nightstand_money}')

    def is_alive(self):
        if self.satiety > 0:
            return self.name

    def live_one_day(self):
        num_cube = randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.refrigerator_food < 10:
            self.shop()
        elif self.house.nightstand_money < 50:
            self.work()
        elif num_cube == 1:
            self.work()
        elif num_cube == 2:
            self.eat()
        else:
            self.play()


class House:
    def __init__(self):
        self.refrigerator_food = 50
        self.nightstand_money = 0

    def __str__(self):
        return (f'еды в холодильнике: {self.refrigerator_food} '
                f'и денег в тумбочке: {self.nightstand_money}.')


def live_year(first_person, second_person):
    for day in range(365):
        print(f'Начинается {day + 1} день')
        if first_person.is_alive():
            first_person.live_one_day()
        else:
            print(f'{first_person.name} умер!!!')
            break
        if second_person.is_alive():
            second_person.live_one_day()
        else:
            print(f'{second_person.name} умер!!!')
            break
        if day + 1 == 365:
            print('\nПрошел целый год!')
        else:
            print(f'Прошло {day + 1} дней!\n')


home = House()
person_1 = Person('Petya', home)
person_2 = Person('Alla', home)
live_year(person_1, person_2)
