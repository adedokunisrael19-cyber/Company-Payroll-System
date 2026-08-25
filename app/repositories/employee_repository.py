from sqlalchemy.orm import Session
from app.models.employee import Employee


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    # CREATE
    def create(self, employee: Employee):
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)

        return employee

    # READ
    def get_by_id(self, employee_id: int):
        return self.db.get(Employee, employee_id)

    def get_all(self):
        return self.db.query(Employee).all()

    def get_by_email(self, email: str):
        return self.db.query(Employee).filter(
            Employee.email == email
        ).first()

    # UPDATE
    def update(self, employee: Employee):
        self.db.commit()
        self.db.refresh(employee)

        return employee

    # DELETE
    def delete(self, employee: Employee):
        self.db.delete(employee)
        self.db.commit()