"""
Паттерн - "Моносостояние". У класса объекты имеют единое локальное простаранство,
единые локальные атрибуты. Изменение одного из атрибутов экземпляра класса
ведет к изменению такого же атрибута другого объекта класса.
"""


class ThreadData:
    """Создаем словарь с общими локальными свойствами экземпляров класса.
    Ключ словаря - свойство объектов, а значение это значение по умолчанию.
    """

    __shared_attrs = {'name': 'thread_1', 'data': {}, 'id': 1}

    def __init__(self):
        """self.__dict__ - хранит локальные свойства экземпляра класса"""
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()

th2.id = 3
if th1.id == 3:
    print(f'Свойства меняются и в другом объекте th1 = {th1.id}')

# Также при созаднии нового свойства, создается этоже свойство в другом классе
th1.attr_new = "new_attr"
print(th2.attr_new)
