import math


class MyMath:
    @classmethod
    def circle_len(cls, radius: float) -> float:
        """
        Вычисляет длину окружности.

        Args:
        - radius (float): Радиус окружности

        Returns:
        - float: Длина окружности
        """
        return 2 * math.pi * radius

    @classmethod
    def circle_square(cls, radius: float) -> float:
        """
        Вычисляет площадь окружности.

        Args:
        - radius (float): Радиус окружности

        Returns:
        - float: Площадь окружности
        """
        return math.pi * (radius ** 2)

    @classmethod
    def cube_volume(cls, side_length: float) -> float:
        """
        Вычисляет объем куба.

        Args:
        - side_length (float): Длина стороны куба

        Returns:
        - float: Объем куба
        """
        return side_length ** 3

    @classmethod
    def sphere_surface_area(cls, radius: float) -> float:
        """
        Вычисляет площадь поверхности сферы.

        Args:
        - radius (float): Радиус сферы

        Returns:
        - float: Площадь поверхности сферы
        """
        return 4 * math.pi * (radius ** 2)


res_1 = MyMath.circle_len(5)
res_2 = MyMath.circle_square(6)
print(res_1)
print(res_2)
