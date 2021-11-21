class Calculator:
    """Принимает два аргумента.
    """

    def __init__(self, x, y):
        """Конструктор класса.
        """
        self.one_argument = x
        self.two_argument = y


class Summa(Calculator):
    """Принимает два родительских и один свой аргумент.
    """

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.three_argument = z

    def calc_summa(self):
        """Этот метод считает сумму трех аргументов.
        """
        summa = 0
        summa = self.one_argument + self.two_argument + self.three_argument
        return summa


class Minus(Calculator):
    """Принимает два родительских и один свой аргумент.
    """

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.three_argument = z

    def calc_minus(self):
        """Этот метод считает разницу трех аргументов.
        """
        minus = 0
        minus = self.one_argument - self.two_argument - self.three_argument
        return minus


def show_result(result):
    """Выводит на печать сумму или разницу.
    """
    if result == calculate_summa:
        print(f'Summa - {result.calc_summa()}')
    else:
        print(f'Minus - {result.calc_minus()}')


calculate_summa = Summa(5, 7, 6)
calculate_minus = Minus(10, 2, 5)
print(f'One number - {calculate_summa.one_argument}')
print(f'Two number - {calculate_summa.two_argument}')
print(f'Three number - {calculate_summa.three_argument}')
show_result(calculate_summa)
print()
print(f'One number - {calculate_minus.one_argument}')
print(f'Two number - {calculate_minus.two_argument}')
print(f'Three number - {calculate_minus.three_argument}')
show_result(calculate_minus)
