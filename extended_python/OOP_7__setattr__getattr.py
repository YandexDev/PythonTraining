"""
Порядок обращения к атрибутам класса и атрибутам его экземпляра.
Изменение своства класса только через @classmethod
Магические методы:
__setattr__(self, key, value) - автоматически вызывается при изменении
свойств класса.
__getatribute__(self, item) - автоматически вызывается при получении
свойства класса с именем item.
__getattr__(self, item) - автоматически вызывается при получении
несуществующего свойства item класса.
__delattr__(self, item) - автоматически вызывается при удалении свойства item
(не важно: существует оно или нет).
"""


class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        """Именение свойств класса в методе класса"""
        cls.MIN_COORD = left

    def __getattribute__(self, item):
        """Вызывается, когда вызывается атрибут через экземпляр класса.
        Например запретить обращаться к атрибуту х"""
        if item == "x":
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """Вызывается, когда идет присвоение
        к какому-либо атрибуту какое-либо значение.
        Можем запретить какой-либо атрибут в экземпляре класса."""
        if key == 'z':
            raise AttributeError("Недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        """Вызывается, когда идет обращение к несуществующему
        атрибуту экземпляра класса.
        Возвращает False"""
        return False

    def __delattr__(self, item):
        """Вызывается, когда удаляется определенный артибут
        из экземпляра класса"""
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.set_bound(-100)
# print(pt1.__dict__)
# print(Point.__dict__)
