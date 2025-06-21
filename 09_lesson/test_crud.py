# pytest test_crud.py -v
# test_crud.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from UsersTable import User, Base

# Используем ту же базу QA для тестов или создаем тестовую в той же структуре
TEST_DATABASE_URL = ("postgresql://sger.skypro:Skypro123456+d@"
                     "localhost:5432/QA_test")


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
    new_user = User(user_email="test@example.com", subject_id=1)
    db_session.add(new_user)
    db_session.commit()

    # Проверяем, что пользователь создан
    user = db_session.query(User).filter(
        User.user_email == "test@example.com"
    ).first()

    assert user is not None
    assert user.user_email == "test@example.com"
    assert user.subject_id == 1

    # Очистка
    db_session.delete(user)
    db_session.commit()


def test_update_user(db_session):
    # Создаем пользователя для теста
    new_user = User(user_email="update@example.com", subject_id=1)
    db_session.add(new_user)
    db_session.commit()

    # Обновляем пользователя
    user = db_session.query(User).filter(
        User.user_email == "update@example.com"
    ).first()

    user.subject_id = 2
    db_session.commit()

    # Проверяем обновление
    updated_user = db_session.query(User).filter(
        User.user_email == "update@example.com"
    ).first()

    assert updated_user.subject_id == 2

    # Очистка
    db_session.delete(updated_user)
    db_session.commit()


def test_get_user_with_subject(db_session):
    # Создаем тестового пользователя
    test_email = f"test_{datetime.now().timestamp()}@example.com"
    new_user = User(user_email=test_email, subject_id=3)
    db_session.add(new_user)
    db_session.commit()

    # Проверяем получение пользователя с subject_id
    user = db_session.query(User).filter(
        User.user_email == test_email,
        User.subject_id == 3
    ).first()

    assert user is not None
    assert user.user_email == test_email
    assert user.subject_id == 3

    # Очистка
    db_session.delete(user)
    db_session.commit()
