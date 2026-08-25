from datetime import date
from typing import Optional
from pydantic import BaseModel

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