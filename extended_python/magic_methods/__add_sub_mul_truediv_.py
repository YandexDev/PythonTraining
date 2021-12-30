"""
Магические методы:
__add__ - для операции сложения
__sub__ - для операции вычитания
__mul__ - для операции умножения
__truediev__ - для операции деления
__floordiv__ - целочисленное деление (14 // 4 = 3)
__mod__ - деление по модулю(взятие остатка) (14 % 3 = 2)
"""


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        """Возвращает строку приписывая незначащий 0"""
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом или clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    def __radd__(self, other):
        """Если в момент сложения целое число слева от объекта класса"""
        return self + other

    def __iadd__(self, other):
        """Если необходимо чтобы работала конструкция +="""
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом или clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self


c1 = Clock(1000)
# Работает благодаря магическому методу __add__
c1 = c1 + 1000  # Равносильно c1.__add__(100)
print(c1.get_time())
c2 = Clock(2000)
c3 = Clock(3000)
c4 = c1 + c2 + c3
print(c4.get_time())
c5 = Clock(1000)
c5 += 100
print(c5.get_time())
