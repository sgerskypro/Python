# Нужно для округления вверх
import math


def square(side):
    area = side * side
    return math.ceil(area)


# Пример
side_length = 4.2
print("Площадь квадрата:", square(side_length))
# Пример использования
print(square(4.2))  # Выведет 18 (4.2*4.2=17.64 → округляем до 18)
