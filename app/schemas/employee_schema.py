from datetime import date

from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    position: str
    base_salary: float
    hire_date: date


class EmployeeUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    position: str | None = None
    base_salary: float | None = None
    hire_date: date | None = None


class EmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    position: str
    base_salary: float
    hire_date: date