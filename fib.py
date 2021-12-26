def fib(n):
    """Функция вычисляет числа Фибоначчи
    n: целое число до 29
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(5)
    10
    """
    if not isinstance(n, int):
        raise TypeError('Должно быть целое число')

    if n < 0:
        raise ValueError('Должно быть положительное число')

    if n >= 30:
        raise ValueError('Должно быть меньше и не равно 30')

    F = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
