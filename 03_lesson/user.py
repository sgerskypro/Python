# user.py
class User:
    def __init__(self, first_name, last_name):
        """
        Конструктор класса User.
        Принимает:
        - first_name (str): имя пользователя
        - last_name (str): фамилия пользователя
        """
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        """Печатает имя пользователя"""
        print(self.first_name)

    def print_last_name(self):
        """Печатает фамилию пользователя"""
        print(self.last_name)

    def print_full_name(self):
        """Печатает полное имя пользователя"""
        print(f"{self.first_name} {self.last_name}")


"""  Создание класса:
class User: - объявляем новый класс с именем User
Конструктор класса:
def __init__(self, first_name, last_name): - метод инициализации (конструктор)
self - обязательный первый параметр, ссылается на создаваемый объект
first_name и last_name - параметры, которые передаются при создании объекта
Инициализация атрибутов:
self.first_name = first_name - создаем атрибут first_name у объекта
self.last_name = last_name - создаем атрибут last_name у объекта"""
