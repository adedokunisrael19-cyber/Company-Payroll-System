from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    position: str
    salary: float
    hire_date: date
    department_id: int