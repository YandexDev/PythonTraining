class Point:
    def __new__(cls, *args, **kwargs):
        """cls ссылается на класс"""
        print("вызов __new__ для " + str(cls))
        # ссылается на родительский класс object (в пайтоне)
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        """init ссылается на объект класса"""
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y
