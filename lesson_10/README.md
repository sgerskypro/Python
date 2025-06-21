# Инструкции по запуску тестов и просмотру отчетов
##  установливаем все необходимые зависимости:
```bash
pip install pytest selenium allure-pytest


# Запуск тестов интернет-магазина:
pytest shop_test.py -v
# Или с генерацией отчета Allure:
pytest shop_test.py --alluredir=allure_results

# Запуск теста калькулятора :
pytest test_calculator.py -v
# Или с генерацией отчета Allure:
pytest test_calculator.py --alluredir=allure_results

# Просмотр отчетов Allure
# Сначала убедиться, что   установлен Allure Commandline.
scoop install allure

# для просмотра отчета после запуска тестов с генерацией отчета Allure:
allure serve allure_results