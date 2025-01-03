import math

class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = []
        self.__color = [1, 1, 1]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def set_color(self, r, g, b):
        self.__color = [r, g, b]

    def get_color(self):
        return self.__color

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__()
        self.set_color(*color)
        if len(sides) == 0:
            self.__sides = [1]
        elif len(sides) == 1:
            self.__sides = [sides[0]]
        else:
            self.__sides = [1]

    def get_square(self):
        radius = self.__sides[0] / (2 * math.pi)
        return math.pi * radius ** 2

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__()
        self.set_color(*color)
        if len(sides) == 0:
            self.__sides = [1] * 12
        elif len(sides) == 1:
            self.__sides = [sides[0]] * 12
        elif len(sides) == 12:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * 12

    def get_volume(self):
        return self.__sides[0] ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
