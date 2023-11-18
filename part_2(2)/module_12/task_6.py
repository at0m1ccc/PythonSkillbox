from abc import ABC


class Shape(ABC):
    @classmethod
    def area(cls):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


print("Площадь круга:", Circle(3).area())
print("Площадь прямоугольника:", Rectangle(2, 10).area())
print("Площадь треугольника:", Triangle(10, 5).area())
