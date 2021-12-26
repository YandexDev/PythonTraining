class Point:
    color = 'Red'
    circle = 2
    # Возвращает строку как имя класса
    # def __str__(self):
    #     return 'Point_name'

    def set_coords(self, x: str):
        """Метод класса (действие)"""
        self.x = x
        print(f'Вызов функции set_coords {str(self)} {x}')

    def get_coords(self):
        return self.x


pt = Point()  # Создание объекта pt
pt2 = Point()  # Создание объекта pt2
# Вызов метода класса. self - принадлежность этому объекту
pt.set_coords('класса Point')
# Тоже самое, но атрибут х переопределили
Point.set_coords(pt, 'объект pt')
pt2.set_coords('объект pt2')
print(pt.__dict__)  # Выводит атрибуты (свойства) объекта
print(pt2.__dict__)

print(pt.get_coords())  # Вызов метода класса через объект
print(pt2.get_coords())  # Вызов метода класса через объект
print(Point.get_coords(pt))  # Вызов метода класса через класс
print(Point.get_coords(pt2))  # Вызов метода класса через класс
