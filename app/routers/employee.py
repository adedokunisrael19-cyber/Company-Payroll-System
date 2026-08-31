from fastapi import APIRouter, HTTPException
from starlette import status

from app.database.database import SessionLocal
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate
from app.services.employee_service import EmployeeService


router = APIRouter()

db_session = SessionLocal()
repository = EmployeeRepository(db_session)
employee_service = EmployeeService(repository)


@router.post("/employees")
def create_employee(employee: EmployeeCreate):
    return employee_service.register_employee(employee)


@router.get("/employees/{id}")
def get_employee(id: int):
    try:
        return employee_service.get_employee(id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )


@router.get("/employees")
def list_employees():
    return employee_service.get_all_employees()


@router.put("/employees/{id}")
def update_employee(id: int, employee: EmployeeUpdate):
    return employee_service.update_employee(id, employee)


@router.delete("/employees/{id}")
def delete_employee(id: int):
    return employee_service.delete_employee(id)