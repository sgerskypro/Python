# Функция проверки високосного года
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


# Проверяем 2024 год
year = 2024
result = is_year_leap(year)
print("год", year, ":", result)
