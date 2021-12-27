"""
Функция, которая удаляет символы в начале и в конце строки
"""


def strip_string(strip_chars=" "):
    """Символы, которые надо удалить"""

    def do_strip(string):
        """Строка, в которой надо их удалить"""
        return string.strip(strip_chars)  # Через метод strip удаляет

    return do_strip


strip1 = strip_string()
strip2 = strip_string(' !&.,;')

print(strip1(' hello python!... '))
print(strip2(' hello python!... '))
