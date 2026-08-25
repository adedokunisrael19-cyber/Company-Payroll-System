from app.database.database import Base, engine
from app.models import Employee, Payroll


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")