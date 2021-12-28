"""
Магические методы:
__str__ - для отображения информации об объекте класса для пользователей
__repr__ - для отображения информации об объекте класса в режиме отладки(dev)
__len__ - позволяет применять функцию len() к экземплярам класса
__abs__ - позволяет применять функцию abs() к экземплярам класса:
получение модуля числа (из отрицательного в положительное)
"""


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """Для разработчиков, в режиме отладки"""
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        """Для пользователей. Например: вызывается при функции print"""
        return self.name


cat = Cat("Васька")
print(cat)


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        # Функция map - применение функци ко всем итерируемым объектам в параметрах
        return list(map(abs, self.__coords))


p = Point(1, 2, -5, -10)
print(len(p))
print(abs(p))
