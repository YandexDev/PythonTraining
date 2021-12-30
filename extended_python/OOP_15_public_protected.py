"""
Наследование. Атрибуты private и protected.
__.attributs - только использование в классе
_.attributs - в классе и в дочерних классах, извне можно обратиться, но не стоит
"""


class Geom:
    def __init__(self, x, y, x1, y1):
        self.__x = x
        self.__y = y
        self.__x1 = x1
        self.__y1 = y1

    def get_coords(self):
        return self.__x, self.__y


class Rect(Geom):
    def __init__(self, x, y, x1, y1, fill="red"):
        super().__init__(x, y, x1, y1)
        self.fill = fill


r = Rect(1, 2, 3, 4, "Green")
g = Geom(4, 3, 2, 1)
print(r.__dict__)
# print(r.__x)  Выдаст ошибку, т.к. атрибут приватный (только для класса)
print(Geom.get_coords(g))
