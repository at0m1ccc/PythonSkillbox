class Property:
    def __init__(self, worth):
        self.worth = worth

    def calc_tax(self):
        return 0


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return self.worth / 500


money = float(input("Введите кол-во денег: "))
property_worth = float(input("Введите стоимость имущества: "))

apartment = Apartment(property_worth)
car = Car(property_worth)
country_house = CountryHouse(property_worth)

apartment_tax = apartment.calc_tax()
car_tax = car.calc_tax()
country_house_tax = country_house.calc_tax()

total_tax = apartment_tax + car_tax + country_house_tax

print(f"Налог на квартиру: {apartment_tax}")
print(f"Налог на машину: {car_tax}")
print(f"Налог на дачу: {country_house_tax}")
print(f"Общий налог: {total_tax}")

if money < total_tax:
    print(f"Вам не хватает {total_tax - money} денег для уплаты налогов!")
else:
    print("Вам хватает денег для уплаты налогов!")
