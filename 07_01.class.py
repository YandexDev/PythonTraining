class Student:
    """Create class Student"""

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def show(self):
        print(f"Name: {self.name}, surname: {self.surname}!")


Andrei = Student("Andrei", "Pervyi")

Andrei.show()

print(dir(Student))
