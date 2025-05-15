# address.py Класс Address хранит все компоненты почтового адреса
class Address:
    def __init__(self, index, city, street, house, apartment):
        """
        Класс для хранения почтового адреса
        """
        self.index = index      # Почтовый индекс
        self.city = city        # Город
        self.street = street    # Улица
        self.house = house      # Дом
        self.apartment = apartment  # Квартира
