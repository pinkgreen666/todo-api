import datetime
from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
    func,
    null,
)
from sqlalchemy.orm import DeclarativeBase, sessionmaker

sqlite_database = "sqlite:///test.db"

engine = create_engine(sqlite_database)


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    is_completed = Column(Boolean, default=datetime.datetime.utcnow)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self) -> str:
        return (
            f"<Task(id={self.id}, title='{self.title}', completed={self.is_comleted})>"
        )


Base.metadata.create_all(bind=engine)

print("База данных и таблица создана")

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
