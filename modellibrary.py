objects = []


def create_objects(name):
    objects.append(f"Objects [{name}]")


def print_objects():
    print("Все добавленные объекты:")
    for obj in objects:
        print(obj)


def foo():
    """Выводит имя модуля"""
    print(__name__)


def bar(x, y):
    """Складывает и возвращает сумму"""
    return x + y


if __name__ == "__main__":
    print("Library executed separately")
