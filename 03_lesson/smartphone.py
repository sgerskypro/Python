# smartphone.py
class Smartphone:
    def __init__(self, brand, model, phone_number):
        """
        Конструктор класса Smartphone. Принимает:
        - brand (str): марка телефона
        - model (str): модель телефона
        - phone_number (str): номер телефона в формате '+79...'
        """
        self.brand = brand          # Марка телефона
        self.model = model          # Модель телефона
        self.phone_number = phone_number  # Номер телефона
