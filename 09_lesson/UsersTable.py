from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(100), unique=True, nullable=False)
    subject_id = Column(Integer)

    def __repr__(self):
        return (
         f"<User(user_id={self.user_id}, "
         f"email='{self.user_email}', "
         f"subject_id={self.subject_id})>"
        )


# Подключение к БД (в конец файла, чтобы избежать циклических импортов)
DATABASE_URL = "postgresql://ваш_пользователь:ваш_пароль@localhost:5432/QA"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Создает таблицы в базе данных"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Генератор сессий для работы с БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
