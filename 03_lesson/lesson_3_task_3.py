# lesson_3_task_3.py
from address import Address
from mailing import Mailing


def create_mailing_example() -> None:
    """Создает и выводит пример почтового отправления."""
    # Создаем адреса
    to_address = Address(
        index="123456",
        city="Москва",
        street="Ленина",
        house="1",
        apartment="101"
    )

    from_address = Address(
        index="654321",
        city="Краснодар",
        street="Красная",
        house="122",
        apartment="122"
    )

    # Создаем почтовое отправление
    mail = Mailing(
        to_address=to_address,
        from_address=from_address,
        cost=500.0,
        track="TRACK123456"
    )

    # Форматированный вывод с разбивкой длинных строк иначе Flake8 с ошибкой
    from_template = (
        f"{mail.from_address.index}, {mail.from_address.city}, "
        f"{mail.from_address.street}, {mail.from_address.house} - "
        f"{mail.from_address.apartment}"
    )

    to_template = (
        f"{mail.to_address.index}, {mail.to_address.city}, "
        f"{mail.to_address.street}, {mail.to_address.house} - "
        f"{mail.to_address.apartment}"
    )

    print(
        f"Отправление {mail.track} из {from_template} "
        f"в {to_template}. Стоимость {int(mail.cost)} рублей."
    )


if __name__ == "__main__":
    create_mailing_example()
