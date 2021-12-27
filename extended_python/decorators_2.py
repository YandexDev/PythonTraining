"""
Декоратор высчитывает время выполнения функциию
Функции - медленный и быстрый алгоритм Ефклида.
"""
import time


def test_time(func):
    """Декоратор для измерения времени выполнения функции"""

    def wrapper(*args, **kwargs):
        #  Начало измерения
        st = time.time()
        # Сама функция
        res = func(*args, **kwargs)
        # Конец измерения
        et = time.time()
        dt = et - st
        print(f"Время работы фунции: {dt} сек.")
        return res

    return wrapper


@test_time  # Декорируем функцию
def get_nod(a, b):
    """Медленный алгоритм Ефклида. Набольший общитель делитель."""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time  # Декорируем функцию
def get_fast_nod(a, b):
    """Быстрый алгоритм Ефклида"""
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a


# get_nod = test_time(get_nod)  # Декорируем функцию
# get_fast_nod = test_time(get_fast_nod)  # Декорируем функцию

res = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)
print(res)
print(res2)
