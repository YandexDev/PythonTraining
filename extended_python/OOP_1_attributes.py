class Point:
    """Класс представления точек на плоскости"""

    color = "Red"
    circle = 2


print(Point.color)
print(Point.circle)
print(Point.__dict__)  # Выводит все свойства (атрибуты) класса

a = Point()
b = Point()

a.color = "Black"  # Переопределил свойство у объекта а класса Point
print(a.color)
print(b.color)
print(a.__dict__)  # Появилось свойство у объекта а
print(b.__dict__)

Point.type_pt = "Name"  # Добавили новое свойста классу
print(Point.type_pt)
setattr(Point, "name", "Andrei")  # Добавили новое свойста классу
print(Point.name)

# Вернет False, если нет такого атрибута
print(getattr(Point, "lenght", False))
# Показать наличие атрибута
print(hasattr(Point, "type_pt"))
# del Point.name Удаление атрибута класса
# delattr(Point, 'name') Удаление атрибута через функцию
