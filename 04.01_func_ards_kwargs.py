def foo(x, y, z=0):
    """z=0 - значение по умолчанию"""
    return x*100 + 10*y + 1*z


print(foo(1, 2, 3))
# Именнованнные параметры
print(foo(z=1, y=2, x=3))
print(foo(1, 2))


def bar(name, *scores):
    """* - множественные параметры"""
    for arg in scores:
        print(name, arg)


bar('Andrei', 45, 656, 324, 4543)


def your_girls_age(name, **girls_age):
    """** - создает список"""
    print(name, girls_age)


your_girls_age('Andrei', Eva=32, Glory=18, Janna=24)
