"""
Декоратор(другая функция) привозносит изменение в функцию,
благодаря замыканию.
Декорируют функцию и расширяют ее функционал.
"""


def func_decorator(func):
    """Замыкание"""

    def wrapper(*args, **kwargs):
        """Принимает фактические и формальные параметры"""
        print('----- что-то делаем перед вызовом функции -----')
        res = func(*args, **kwargs)
        print('----- что-то делаем перед вызовом функции -----')
        return res

    return wrapper


def some_func(title, tag):
    print(f"Вызов функции some_func - {title} с тегом {tag}")
    return f"<{tag}><{title}></{tag}>"


some_func = func_decorator(some_func)
res = some_func("Python навсегда!", "h1")
print(res)
