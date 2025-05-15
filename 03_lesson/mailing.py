# mailing.py
from address import Address  # Импорт используется в аннотациях типов


class Mailing:
    def __init__(self,
                 to_address: Address,   # Указываем тип Address
                 from_address: Address,  # Указываем тип Address
                 cost: float,
                 track: str):
        """
        Класс для описания почтового отправления
        Аргументы:
        - to_address (Address): адрес получателя
        - from_address (Address): адрес отправителя
        - cost (float): стоимость отправления
        - track (str): трек-номер
        """
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
