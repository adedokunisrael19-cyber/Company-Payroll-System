from app import Base, engine
from app import Employee, Payroll


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")