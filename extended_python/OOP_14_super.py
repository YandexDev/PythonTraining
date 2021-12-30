"""
Что такое расширение (extended) классов и переопределение (overriding) методов.
Функция super() для обращения к атрибутам базового класса и вызова его методов.
Делегированный вызов на примере инициализаторов классов.
"""


class Geom:
    name = "Geom"

    def __init__(self, x, y, z, b):
        self.coord1 = x
        self.coord2 = y
        self.coord3 = z
        self.coord4 = b

    def draw(self):
        print("Рисует геометрическую фигуру")


class Rect(Geom):
    """super() - возвращает объект посредник родительского класса"""

    name = "Rect"  # Переопределение свойства

    def __init__(self, x, y, z, b, fill):
        super().__init__(x, y, z, b)
        self.rect_fill = fill

    def draw(self):
        print("Рисует квадрат(rectangle)")  # Переопределение метода

    def get_coord(self):
        print(self.__dict__)  # Выводит атрибуты дочернео класса (расширяет)


rect = Rect(1, 2, 3, 4, "Red")
print(rect.coord1, rect.coord2)
rect.get_coord()
