"""
Пример использования декоратора @property:
Метод .split() - разделяет строку по разделителю - пробелу, получая список срок
Метод .strip() - удаляет в строке все пробелы, если не указано другое(.strip('*'))
метод .isdigit() - возвращает True, если строка состоит из чисел и пробелов, и имеет хотя бы один символ
"""
# Импортирует все латинские буквы
from string import ascii_letters


class Person:
    """
    Создаем класс Person с ФИО, возрастом, паспортными данными и весом.
    """

    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        """Ниже проверку валидации можно не указывать,
        а в объявлении переменных указать принадлежность через
        сеттер @property(кроме фио, т.к. в ФИО не указывали сеттер:
        self.old = old
        self.ps = ps
        self.weight = weight
        """
        self.verify_fio(fio)  # Проверка на валидацию ФИО
        self.verify_old(old)  # Проверка на валидацию возраста
        self.verify_weight(weight)  # Проверка на валидацию веса
        self.verify_ps(ps)  # Проверка на валидацию по паспорту

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        """Валидация ФИО"""
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError(
                    "В ФИО можно использовать только буквенные символы и дефис"
                )

    @classmethod
    def verify_old(cls, old):
        """Валидация возраста"""
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст - целое число от 14 до 120")

    @classmethod
    def verify_weight(cls, weight):
        """Валидация веса"""
        if type(weight) != float or weight < 20:
            raise TypeError("Вес должен быть вещественным числом от 20")

    @classmethod
    def verify_ps(cls, ps):
        """Валидация паспорта"""
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    # Ниже интерфейсы для взаимодействия с этими приватными данными
    @property
    def fio(self):
        """Создание геттера для получения доступа к ФИО"""
        return self.__fio

    @property
    def old(self):
        """Создание геттера для получения доступа к возрасту"""
        return self.__old

    @old.setter
    def old(self, old):
        """Создание сеттера для изменения возраста.
        Метод должен называтся также как и геттер"""
        self.verify_old(old)  # Валидация
        self.__old = old

    @property
    def weight(self):
        """Создание геттера для получения доступа к весу"""
        return self.__weight

    @weight.setter
    def weight(self, weight):
        """Создание сеттера для изменения веса.
        Метод должен называтся также как и геттер"""
        self.verify_weight(weight)  # Валидация
        self.__weight = weight

    @property
    def passport(self):
        return self.__ps

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__ps = ps


p = Person('Первый Андрей Вячеславович', 35, '1234 567890', 80.0)
# Изменение через модели @property - сеттеры
p.old = 20
p.passport = '4567 123456'
p.weight = 80.0
print(p.__dict__)
# Получение через модели @property - геттеры
print(p.fio)
print(p.old)
# Выбросит исключение
p.old = 200
print(p.old)
