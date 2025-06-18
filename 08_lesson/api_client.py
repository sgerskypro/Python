"""
api_client.py - Клиент для работы с API управления проектами YouGile

Этот файл содержит класс ProjectsApi для взаимодействия с YouGile API:
- Создание проектов
- Получение информации о проектах
- Обновление проектов
- Получение списка проектов компании

использует переменные окружения для безопасного хранения токена.
Токен должен быть указан в файле .env как YOUGILE_API_TOKEN.
"""

import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()


class ProjectsApi:
    """Основной класс для работы с API проектов YouGile"""

    def __init__(self, base_url):
        """
        Инициализация клиента API

        :param base_url: Базовый URL API (например "https://ru.yougile.com/api-v2")
        """
        self.base_url = base_url
        self.token = self._get_auth_token()

    def _get_auth_token(self):
        """
        Получение токена из переменных окружения

        :raises ValueError: Если токен не найден в .env
        :return: API токен
        """
        token = os.getenv('YOUGILE_API_TOKEN')
        if not token:
            raise ValueError(
                "API токен не найден. Добавьте YOUGILE_API_TOKEN в .env файл\n"
                "Пример содержимого .env:\n"
                "YOUGILE_API_TOKEN=ваш_токен_доступа\n"
                "YOUGILE_COMPANY_ID=ваш_id_компании"
            )
        return token

    def _get_headers(self):
        """Возвращает стандартные заголовки с токеном авторизации"""
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

    def new_project(self, title, users=None):
        """
        Создание нового проекта

        :param title: Название проекта
        :param users: Словарь {user_id: role} (опционально)
        :return: Response object
        """
        payload = {
            "title": title,
            "users": users or {}
        }
        response = requests.post(
            f"{self.base_url}/projects",
            headers=self._get_headers(),
            json=payload
        )
        return response

    def get_project_by_id(self, project_id):
        """
        Получение проекта по ID

        :param project_id: UUID проекта
        :return: Response object
        """
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self._get_headers()
        )

    def get_list_of_company_projects(self):
        """Получение списка всех проектов компании"""
        return requests.get(
            f"{self.base_url}/projects/",
            headers=self._get_headers()
        )

    def update_project(self, project_id, title, users=None):
        """
        Обновление существующего проекта

        :param project_id: UUID проекта
        :param title: Новое название
        :param users: Обновленный словарь {user_id: role} (опционально)
        :return: Response object
        """
        payload = {
            "title": title,
            "users": users or {}
        }
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self._get_headers(),
            json=payload
        )

        # Логирование для отладки
        print(f"Статус обновления: {response.status_code}")
        print(f"Ответ сервера: {response.text}")

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            print(f"Ошибка обновления проекта: {str(e)}")

        return response
