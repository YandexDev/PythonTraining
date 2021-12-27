"""
Создание фунции через замыкание,
которая при каждом своем вызове увеличивает значение на единицу
"""


def counter(start=0):
    def step():
        nonlocal start  # Чтобы использовать переменную из внешнего окружения
        start += 1
        return start

    return step


c1 = counter(10)
c2 = counter()
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
