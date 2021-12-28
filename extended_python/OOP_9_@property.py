"""
Для работы с приватными атрибутами, вместо сетторов и геттеров.
Переводится - свойство.
"""


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property  # Геттер
    def old(self):
        return self.__old

    @old.setter  # Из @property
    def old(self, old):
        self.__old = old

    @old.deleter  # Из @property
    def old(self):
        del self.__old


p = Person('Андрей', 20)
p.old = 35
print(p.old, p.__dict__)
