from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    position: str
    salary: float
    hire_date: date
    department_id: int

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
    department_id: Optional[int] = None
    status: Optional[str] = None


class EmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    position: str
    salary: float
    hire_date: date
    department_id: int
    department_name: Optional[str] = None
    status: str