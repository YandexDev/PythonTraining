def main():
    value_summa = Summa(10, 20)
    value_summa.show_paramets_summa()
    value_summa.count_summa()
    print()
    value_minus = Minus(30, 10, 5)
    value_minus.show_paramets_minus()
    value_minus.count_minus()


class Calculate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Summa(Calculate):

    def show_paramets_summa(self):
        print(f'Заданные параметры: {self.x} и {self.y}')

    def count_summa(self):
        print('Сумма значений равна:', self.x + self.y)


class Minus(Calculate):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self.z = z

    def show_paramets_minus(self):
        print(f'Заданные параметры: {self.x}, {self.y} и {self.z}')

    def count_minus(self):
        print('Минус трех значений равна:', self.x - self.y - self.z)


main()
