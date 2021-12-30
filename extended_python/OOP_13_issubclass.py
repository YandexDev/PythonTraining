"""
Наследование от встроенных типов (iny, string, list и т.д. - классы) и от object.
Функция - issubclass():
issubclass(Class1, Class1) -> True:
Class1 - дочерний класс
Class2 - родительский класс
Функция isinstance(obj, Class) -> True:
obj - объект класса Class (даже если класс родительский)
"""


class Geom:
    name = "Геометрия"

    def __str__(self):
        return "Строковое имя Геометрия"


class Line(Geom):
    pass


g = Geom()
line = Line()
# print(g)
# print(g.__class__)
# print(g.__module__)
# print(Geom.__dict__)
# print(Geom.__str__(g))
# print()
# print(Line.__dict__)
# print(Line.__str__(line))
