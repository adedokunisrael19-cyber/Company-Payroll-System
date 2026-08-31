from app.models.employee import Employee
class EmployeeRepository:

    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, employee):
        self.db_session.add(employee)
        self.db_session.commit()
        self.db_session.refresh(employee)

        return employee

    def find_by_id(self, id):
        return self.db_session.get(Employee, id)

    def find_by_email(self, email):
        return self.db_session.query(Employee).filter(
            Employee.email == email
        ).first()

    def get_all(self):
        return self.db_session.query(Employee).all()

    def update(self, employee):
        self.db_session.commit()
        self.db_session.refresh(employee)

        return employee

    def delete(self, employee):
        self.db_session.delete(employee)
        self.db_session.commit()