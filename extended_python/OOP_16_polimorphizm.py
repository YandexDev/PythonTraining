"""
Полиморфизм - это называть методы одинакого для классов
get_pr - Абстрактный метод
Абстрактный метод - должен быть переопределен в дочерних классах. Не имеет
собственной реализации в базовом классе.
"""


class Geom:
    def get_pr(self):
        raise NotImplementedError(
            "В дочернем классе должен быть определен метод get_pr()"
        )


class Rectangle(Geom):
    """Вычисление периметра фигуры"""

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        """Если этот метод отсутвует, то выбрасывается исключение"""
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [
    Rectangle(1, 2),
    Rectangle(3, 4),
    Square(10),
    Square(20),
    Triangle(1, 2, 3),
    Triangle(4, 5, 6),
]
# print(r1.get_pr(), r2.get_pr())
# print(s1.get_pr(), s2.get_pr())
# print(t1.get_pr(, t2.get_pr()))
for g in geom:
    print(g.get_pr())
