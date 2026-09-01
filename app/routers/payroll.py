from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.repositories.payroll import PayrollRepository
from app.schemas.payroll import PayrollResponse, PayrollCreateSchema, PayrollUpdate
from app.services.payroll import PayrollService
from app.database.database import get_db

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


def get_payroll_service(
    db: Session = Depends(get_db)
) -> PayrollService:

    repository = PayrollRepository(db)

    return PayrollService(repository)


@router.post(
    "",
    response_model=PayrollResponse,
    status_code=status.HTTP_201_CREATED
)
def create_payroll(
    data: PayrollCreateSchema,
    service: PayrollService = Depends(get_payroll_service)
):
    return service.create_payroll(data)


@router.get(
    "",
    response_model=list[PayrollResponse]
)
def get_all_payrolls(
    service: PayrollService = Depends(get_payroll_service)
):
    return service.get_all_payroll()


@router.get(
    "/employee/{employee_id}",
    response_model=list[PayrollResponse]
)
def get_employee_payrolls(
    employee_id: int,
    service: PayrollService = Depends(get_payroll_service)
):
    return service.get_employee_payroll(employee_id)


@router.get(
    "/{payroll_id}",
    response_model=PayrollResponse
)
def get_payroll(
    payroll_id: int,
    service: PayrollService = Depends(get_payroll_service)
):
    try:
        return service.get_payroll(payroll_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payroll not found"
        )


@router.put(
    "/{payroll_id}",
    response_model=PayrollResponse
)
def update_payroll(
    payroll_id: int,
    data: PayrollUpdate,
    service: PayrollService = Depends(get_payroll_service)
):
    try:
        return service.update_payroll(
            payroll_id,
            data
        )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payroll not found"
        )


@router.delete(
    "/{payroll_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_payroll(
    payroll_id: int,
    service: PayrollService = Depends(get_payroll_service)
):
    try:
        service.delete_payroll(payroll_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payroll not found"
        )