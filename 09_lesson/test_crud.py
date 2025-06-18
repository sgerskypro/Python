# pytest test_crud.py -v
# test_crud.py
import pytest
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from UsersTable import User, Base

# Используем ту же базу QA для тестов или создаем тестовую в той же структуре
TEST_DATABASE_URL = "postgresql://sger.skypro:Skypro123456+d@localhost:5432/QA_test"


@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


def test_create_user(db_session):
    # Тест создания пользователя
    new_user = User(name="Test User", email="test@example.com")
    db_session.add(new_user)
    db_session.commit()

    # Проверяем, что пользователь создан и не удален
    user = db_session.query(User).filter(
        and_(
            User.email == "test@example.com",
            User.deleted_at == None
        )
    ).first()

    assert user is not None
    assert user.name == "Test User"
    assert user.email == "test@example.com"

    # Очистка
    db_session.delete(user)
    db_session.commit()


def test_update_user(db_session):
    # Создаем пользователя для теста
    new_user = User(name="Update Test", email="update@example.com")
    db_session.add(new_user)
    db_session.commit()

    # Обновляем пользователя
    user = db_session.query(User).filter(
        and_(
            User.email == "update@example.com",
            User.deleted_at == None
        )
    ).first()

    user.name = "Updated Name"
    db_session.commit()

    # Проверяем обновление
    updated_user = db_session.query(User).filter(
        and_(
            User.email == "update@example.com",
            User.deleted_at == None
        )
    ).first()

    assert updated_user.name == "Updated Name"

    # Очистка
    db_session.delete(updated_user)
    db_session.commit()


def test_soft_delete_user(db_session):
    # 1. Создаем тестового пользователя с уникальным email
    test_email = f"test_{datetime.now().timestamp()}@example.com"
    new_user = User(name="Test User", email=test_email)
    db_session.add(new_user)
    db_session.commit()

    # 2. Проверяем создание
    user = db_session.query(User).filter(
        and_(
            User.email == test_email,
            User.deleted_at == None
        )
    ).first()
    assert user is not None, "Пользователь не был создан"

    # 3. Мягкое удаление
    user.soft_delete()
    db_session.commit()

    # 4. Проверяем мягкое удаление
    deleted_user = db_session.query(User).filter(
        User.email == test_email
    ).first()

    assert deleted_user is not None, "Пользователь должен остаться в базе"
    assert deleted_user.deleted_at is not None, "Поле deleted_at должно быть установлено"

    # 5. Проверяем недоступность в обычных запросах
    active_user = db_session.query(User).filter(
        and_(
            User.email == test_email,
            User.deleted_at == None
        )
    ).first()
    assert active_user is None, "Удалённый пользователь доступен в обычном запросе"

    # 6. Очистка
    db_session.query(User).filter(User.email == test_email).delete()
    db_session.commit()
