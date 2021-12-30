class DataBase:
    """
    Если мы хотим чтобы в классе был только один объект.
    Паттерн проектирования Singleton.
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        """Метод финализатор. При удаление объекта."""
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие соединения с БД")

    def read(self):
        print("Данные из БД")

    def write(self, data):
        print(f"Запись в БД {data}")


db = DataBase("root", "1234", 80)
db2 = DataBase("root2", "12345", 40)
# Второй объект не создается,
# переменная db2 ссылается на тот же самый объект
print(id(db))
print(id(db2))
