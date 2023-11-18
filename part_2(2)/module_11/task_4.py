class WaterElem:

    def __add__(self, other):
        if isinstance(other, AirElem):
            return StormElem()
        elif isinstance(other, FireElem):
            return SteamElem()
        elif isinstance(other, EarthElem):
            return DirtElem()
        else:
            return None


class AirElem:

    def __add__(self, other):
        if isinstance(other, WaterElem):
            return StormElem()
        elif isinstance(other, FireElem):
            return LightningElem()
        elif isinstance(other, EarthElem):
            return DustElem()
        else:
            return None


class FireElem:

    def __add__(self, other):
        if isinstance(other, WaterElem):
            return SteamElem()
        elif isinstance(other, AirElem):
            return LightningElem()
        elif isinstance(other, EarthElem):
            return LavaElem()
        else:
            return None


class EarthElem:

    def __add__(self, other):
        if isinstance(other, WaterElem):
            return DirtElem()
        elif isinstance(other, AirElem):
            return DustElem()
        elif isinstance(other, FireElem):
            return LavaElem()
        else:
            return None


class StormElem:

    def __str__(self):
        return 'Шторм'


class SteamElem:

    def __str__(self):
        return 'Пар'


class DirtElem:

    def __str__(self):
        return 'Грязь'


class LightningElem:

    def __str__(self):
        return 'Молния'


class DustElem:

    def __str__(self):
        return 'Пыль'


class LavaElem:

    def __str__(self):
        return 'Лава'


water = WaterElem()
air = AirElem()
fire = FireElem()
earth = EarthElem()

print(f'Вода + Воздух = {water + air}')

print(f'Вода + Огонь = {water + fire}')

print(f'Вода + Земля = {water + earth}')

print(f'Воздух + Огонь = {air + fire}')

print(f'Воздух + Земля = {air + earth}')

print(f'Огонь + Земля = {fire + earth}')
