"""
Метод класса - @classmetod
"""


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """Метод класса проверяет входит ли параметр метода
        в диапазон числовых аргументов класса. Возвращает True.
        cls - ссылка на текущий класс"""
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        """Использование метода класса. В данном примере проверка на вхожесть
        в диапазон числовых аргументов класса"""
        self.x = self.y = 0
        # if Vector.validate(x) and Vector.validate(y):  Одно и тоже
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y


v = Vector(1, 200)  # 200 не входит диапазон, поэтому x = y = 0
# Вызов метода класса
print(Vector.validate(5))
res = v.get_coords()  # Вызов метода через объект
# res = Vector.get_coords(v)  Тот же самый вызов, но через класс
print(res)
