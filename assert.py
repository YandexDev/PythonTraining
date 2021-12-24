def summa(a: int, b: int) -> int:
    """При проверки в assert выкидывает ошибку"""

    z = a - b
    assert a == z - b, "Ошибка в формуле"
    return z


if __name__ == "__main__":
    print(summa(5, 10))
