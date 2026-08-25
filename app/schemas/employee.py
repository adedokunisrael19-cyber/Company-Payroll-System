from datetime import date
from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str | None = None
    hire_date: date
    salary: float


class EmployeeUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    hire_date: date | None = None
    salary: float | None = None


class EmployeeResponse(BaseModel):
    id: int
    employee_number: str
    first_name: str
    last_name: str
    email: str
    phone: str | None
    hire_date: date
    salary: float