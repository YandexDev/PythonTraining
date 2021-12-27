"""
Метод - @staticmethod.
Данный метод(функция) не имеет отношения ни к методу класса,
ни к методу экземпляров класса(объектам).
"""


class Vector:
    @staticmethod
    def norm2(x, y):
        """Не нужно указывать ни self, ни cls."""
        return x * x + y * y


print(Vector.norm2(10, 20))
