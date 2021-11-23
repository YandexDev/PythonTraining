def main():
    andreika = Human()
    zorg = Aliens()
    andrei = Men()
    andrei.work()
    andreika.see()
    zorg.speak()


class Human:
    def __init__(self):
        pass

    def speak(self):
        print('Я говорю!')

    def move(self):
        print('Я двигаюсь!')

    def see(self):
        print('Я вижу')


class Men(Human):
    def work(self):
        print('Я мужчина, я работаю!')


class Women(Human):
    def home(self):
        print('Я женщина, я дома!')


class Aliens:
    def __init__(self):
        pass

    def speak(self):
        print('Я говорю!')

    def move(self):
        print('Я двигаюсь!')

    def see(self):
        print('Я вижу')


main()
