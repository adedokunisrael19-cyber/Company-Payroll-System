from ast import List

from pygments.lexers import data

from app.models import payroll
from app.models.payroll import Payroll
from app.repositories.payroll import PayrollRepository
from app.schemas.payroll import PayrollCreateSchema, PayrollUpdate


class PayrollService:
    def __init__(self, repository: PayrollRepository):
        self.repository = repository

    def create_payroll(self, data: PayrollCreateSchema) -> Payroll:
        net_salary = (
            data.basic_salary + data.allowances - data.deductions
        )

        payroll = Payroll(
            employee_id=data.employee_id,
            pay_period=data.pay_period,
            basic_salary=data.basic_salary,
            allowances=data.allowances,
            deductions=data.deductions,
            net_salary=net_salary,
            payment_date=data.payment_date,
            status=data.status.value
        )

        return self.repository.create(payroll)


    def get_payroll(self, payroll_id: int) -> Payroll:
        payroll = self.repository.get_by_id(payroll_id)

        if payroll is None:
            raise ValueError("Payroll does not exist")
        return payroll

    def get_all_payroll(self) -> List[Payroll]:
        return self.repository.get_all()

    def get_employee_payroll(self, employee_id: int) -> Payroll:
        return self.repository.get_by_employee_id(employee_id)

    # def update_payroll(self, payroll_id: int, data: PayrollUpdate) -> Payroll:
    #     payroll = self.repository.get_by_id(payroll_id)
    #     if payroll is None:
    #         raise ValueError("Payroll does not exist")
    #     update_data = data.model_dump(
    #         exclude_unset= True
    #     )
    # for field, value in update_data.items():
    #     if field == "status":
    #         value = value.value
    #     setattr(payroll, field, value)
    #
    # payroll.net_salary = (payroll.basic_salary + payroll.allowances - payroll.deductions)
    #
    # return payroll

    def delete_payroll(self, payroll_id: int) -> None:
        payroll = self.repository.get_by_id(payroll_id)

        if payroll is None:
            raise ValueError("Payroll does not exist")
        self.repository.delete(payroll)
