"""
 позитивные и негативные тесты для:
- Создания проектов
- Получения проектов
- Обновления проектов
- Получения списка проектов
"""
# pytest -v
import pytest
import time
from time import sleep
from api_client import ProjectsApi  # Импорт из нашего исправленного файла

# Инициализация клиента API
api = ProjectsApi("https://ru.yougile.com/api-v2")


@pytest.fixture(autouse=True)
def add_delay_after_test():
    """Фикстура для добавления задержки между тестами"""
    yield
    sleep(1)  # 1 секунда задержки между тестами


def test_create_project_success(request):
    """Позитивный тест создания проекта с валидными данными"""
    test_name = request.node.name
    title = f"TestPro_{test_name}"
    users = None

    # Вызов API
    response = api.new_project(title, users)
    project_data = response.json()

    # Проверки
    assert response.status_code == 201, "Неверный статус код"
    assert "id" in project_data, "В ответе отсутствует ID проекта"

    # Проверка через GET запрос
    get_response = api.get_project_by_id(project_data["id"])
    project = get_response.json()

    assert project["title"] == title, "Название проекта не совпадает"
    assert project["id"] == project_data["id"], "ID проекта не совпадает"


def test_create_project_without_title():
    """Негативный тест: создание проекта без названия"""
    response = api.new_project("", None)
    assert response.status_code == 400, "Ожидалась ошибка 400"
    assert "error" in response.json(), "Нет сообщения об ошибке"


def test_update_project_success():
    """Позитивный тест обновления проекта"""
    # Создаем тестовый проект с уникальным именем
    timestamp = str(int(time.time()))  # Using timestamp for uniqueness
    title = "InitialTitle_" + timestamp
    create_response = api.new_project(title, None)
    project_id = create_response.json()["id"]

    # Обновляем проект
    new_title = "UpdatedTitle_" + timestamp
    update_response = api.update_project(project_id, new_title, None)

    # Проверки
    assert update_response.status_code == 200, "Неверный статус код"

    # Проверяем обновление
    get_response = api.get_project_by_id(project_id)
    project = get_response.json()
    assert project["title"] == new_title, "Название не обновилось"
    assert project["users"] == {}, "Список пользователей должен быть пустым"


def test_update_project_without_id():
    """Негативный тест: обновление несуществующего проекта"""
    response = api.update_project(None, "NewTitle", None)
    assert response.status_code == 404, "Ожидалась ошибка 404"
    assert "error" in response.json(), "Нет сообщения об ошибке"






def test_project_in_company_list():
    """Позитивный тест: проверка отображения проекта в списке компании"""
    # Создаем тестовый проект с уникальным именем
    timestamp = str(int(time.time()))  # Используем timestamp для уникальности
    title = "ListTest_" + timestamp
    create_response = api.new_project(title, None)
    project_id = create_response.json()["id"]
    
    # Получаем список проектов
    list_response = api.get_list_of_company_projects()
    projects = list_response.json()
    
    # Проверяем наличие нашего проекта
    found = False
    for project in projects.get("content", []):
        if project["id"] == project_id:
            assert project["title"] == title, "Название проекта не совпадает"
            assert project["users"] == {}, "Список пользователей должен быть пустым"
            found = True
            break
    
    assert found, "Проект не найден в списке"




def test_get_nonexistent_project():
    """Негативный тест: получение несуществующего проекта"""
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project_by_id(invalid_id)
    
    assert response.status_code == 404, "Ожидалась ошибка 404"
    error_data = response.json()
    assert error_data.get("message") == "Проект не найден", "Неверное сообщение об ошибке"
    assert error_data.get("error") == "Not Found", "Неверный тип ошибки"