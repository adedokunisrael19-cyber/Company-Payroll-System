from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "mysql+pymysql://root:1234@localhost/company_payroll"
# I think connects SQLAlchemy to MySQL. SAM check it oo
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass