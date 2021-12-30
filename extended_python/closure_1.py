"""
Замыкание функций
"""


def say_name(name):
    """
    Через переменную f идет замыкание в функцию say_name,
    внутренняя функция say_goodbye замыкает функцию say_name
    """

    def say_goodbye():
        print("Don't say me goodbye, " + name + "!")

    return say_goodbye


f = say_name("Andrei")
#  При каждой новой переменной создается новое окружение
f2 = say_name("Python")
f()
f2()
