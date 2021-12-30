"""
Декоратор для вычисления производной функции.
Декораторы с параметрами, можно дополнительно передавать аргументы.
wraps - необходимо чтобы __name__ и __doc__ сохраняли свои значения,
а не значения вложенной функции декоратора.
"""
import math

from functools import wraps


def df_decorator(dx=0.01):
    """Для обозначения параметра"""

    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # Можно не указывать, т.к. импортируем wraps
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__

        return wrapper

    return func_decorator


@df_decorator(dx=0.01)
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi / 3)
print(df)
