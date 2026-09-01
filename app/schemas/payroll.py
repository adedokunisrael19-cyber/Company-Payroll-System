from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.schemas.payrollStatus import PayrollStatus


class PayrollUpdate(BaseModel):
    pay_period: str | None = None
    basic_salary: Decimal | None = None
    allowances: Decimal | None = None
    deductions: Decimal | None = None
    payment_date: date | None = None
    status: PayrollStatus | None = None


class PayrollCreateSchema(BaseModel):
    employee_id: int
    pay_period: str
    basic_salary: Decimal
    allowances: Decimal = Decimal( "0.00")
    deductions: Decimal = Decimal("0.00")
    payment_date: date | None = None
    status: PayrollStatus = PayrollStatus.PENDING


class PayrollResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    employee_id: int
    pay_period: str
    basic_salary: Decimal
    allowances: Decimal
    deductions: Decimal
    net_salary: Decimal
    payment_date: date | None
    status: PayrollStatus | None = None