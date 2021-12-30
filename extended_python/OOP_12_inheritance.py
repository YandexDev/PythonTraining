"""
Наследование - это когда один класс определяется на основе другого.
Переопределение - это когда атрибут (свойство или метод) переопределяется в 
дочернем классе (изменяется).
"""


class Geom:
    name = "Geom"

    def set_coords(self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        print("Устанавилвает координаты")

    def draw(self):
        print("Рисует: " + self.__str__())


class Line(Geom):
    def __str__(self):
        return "Линия"


class Rect(Geom):
    def __str__(self):
        return "Прямоугольник"


g = Geom()
line = Line()
r = Rect()
line.set_coords(1, 2, 3, 4)
Rect.set_coords(r, 1, 2, 3, 4)
line.draw()
Rect.draw(r)
Rect.draw(line)
