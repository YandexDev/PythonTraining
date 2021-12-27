class Point:
    color = 'Red'
    circle = 2

    def __init__(self, x, y):
        """Инициализатор объекта класса"""
        self.x = x
        self.y = y

    def __del__(self):
        """Удаление экземпляра класса,
        если переменная pt будет переопределена"""
        print('Удаление ' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point(1, 2)
print(pt.__dict__)
