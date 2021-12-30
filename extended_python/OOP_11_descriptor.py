"""
Дескрипторты. data descriptor and non-data descriptor.
Дескрипторы данных, если есть сеттер и делитер(можно менять и удалять)
Non-data descriptor - если необходимо только считывать данные.

"""


class ReadIntEx:
    """Дикриптор не данных, non-data descriptor"""

    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:
    """Дискриптор data, т.к. есть сеттер(изменение) и делитер(удаление) даннных"""

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntEx()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
p.__dict__["xr"] = 5
print(p.xr, p.__dict__)
