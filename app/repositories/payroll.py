

from sqlalchemy.orm import Session

from app.models.payroll import Payroll


class PayrollRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payroll:Payroll) -> Payroll:
        self.db.add(payroll)
        self.db.commit()
        self.db.refresh(payroll)

        return payroll

    def get_by_id(self, payroll_id: int):
        return (
            self.db.query(Payroll)
            .filter(Payroll.id == payroll_id)
            .first()
        )

    def get_all(self):
        return (
            self.db.query(Payroll).all()
        )

    def get_by_employee_id(self, employee_id:int):
        return (
            self.db.query(Payroll)
            .filter(Payroll.employee_id == employee_id)
            .all()
        )

    def update(self, payroll: Payroll) -> Payroll:
        self.db.commit()
        self.db.refresh(payroll)

        return payroll

    def delete(self, payroll_id:int) -> None:
        self.db.delete(payroll_id)
        self.db.commit()


