# from sqlalchemy import create_engine
# from sqlalchemy.orm import DeclarativeBase, sessionmaker
#
#
# DATABASE_URL = "mysql+pymysql://root:banditt@localhost:3306/company_payroll"
# engine = create_engine(DATABASE_URL)
#
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
#
#
# class Base(DeclarativeBase):
#     pass
#
# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import StaticPool


DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()