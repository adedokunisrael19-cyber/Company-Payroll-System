from typing import Optional
from pydantic import BaseModel

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
    department_id: Optional[int] = None
    status: Optional[str] = None