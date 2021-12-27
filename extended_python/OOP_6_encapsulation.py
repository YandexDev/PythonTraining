"""Механизм инкапсуляции:
public - публичный атрибут
_protected - только в классе и дочерних классах
__private - только внутри класса.
Интерфейсные методы - сеттеры, геттеры - нужны для обращения к внутренним
защищенным атрибутам класса извне.
pip install accessify
from accessify import private, protected
@private and @protected - делают методы привытными и защищенными.
"""


class Point:
    @classmethod
    def __check_value(cls, x):
        """Приватный метод. Проверка на соотношения типов."""
        return type(x) in (int, float)

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    def set_coords(self, x, y):
        """Сеттер. Данный проверяет на допустимость типов параметров"""
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coords(self):
        """Геттер"""
        return self.__x, self.__y


pt = Point()
pt.set_coords(10, 40)
print(pt.get_coords())
print(dir(pt))  # Показывает свойства объекта
