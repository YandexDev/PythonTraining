class Student:
    """Create class Student"""

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def show(self):
        print(f"Name: {self.name}, surname: {self.surname}!")


andrei = Student("Andrei", "Pervyi")

andrei.show()
# print(dir(Student))  # Выводит все модули класса
# print(Student.__dict__)
print(andrei.name)  # Выводит атрибут класса
print(andrei.surname)  # Выводит атрибут класса
