

from datetime import date
from decimal import Decimal
from unittest.mock import MagicMock

import pytest

from app.models.payroll import Payroll
from app.schemas.payroll import PayrollCreateSchema, PayrollUpdate
from app.services.payroll import PayrollService


def create_payroll():
    return Payroll(
        id=1,
        employee_id=1,
        pay_period="August 2026",
        basic_salary=Decimal("500000.00"),
        allowances=Decimal("50000.00"),
        deductions=Decimal("20000.00"),
        net_salary=Decimal("530000.00"),
        payment_date=date(2026, 8, 30),
        status="PENDING",
    )




def test_create_payroll():
    repository = MagicMock()
    service = PayrollService(repository)

    data = PayrollCreateSchema(
        employee_id=1,
        pay_period="August 2026",
        basic_salary=Decimal("500000.00"),
        allowances=Decimal("50000.00"),
        deductions=Decimal("20000.00"),
        payment_date=date(2026, 8, 30),
    )

    payroll = create_payroll()
    repository.create.return_value = payroll

    result = service.create_payroll(data)

    repository.create.assert_called_once()

    created_payroll = repository.create.call_args[0][0]

    assert created_payroll.employee_id == 1
    assert created_payroll.basic_salary == Decimal("500000.00")
    assert created_payroll.allowances == Decimal("50000.00")
    assert created_payroll.deductions == Decimal("20000.00")

    assert created_payroll.net_salary == Decimal("530000.00")
    assert result == payroll

def test_get_payroll():
    repository = MagicMock()
    service = PayrollService(repository)

    payroll = create_payroll()

    repository.get_by_id.return_value = payroll

    result = service.get_payroll(1)

    repository.get_by_id.assert_called_once_with(1)

    assert result == payroll

def test_get_payroll_not_found():
    repository = MagicMock()
    service = PayrollService(repository)

    repository.get_by_id.return_value = None

    with pytest.raises(ValueError, match="Payroll does not exist"):
        service.get_payroll(999)

    repository.get_by_id.assert_called_once_with(999)

def test_get_all_payrolls():
    repository = MagicMock()
    service = PayrollService(repository)

    payrolls = [
        create_payroll(),
        create_payroll(),
    ]

    repository.get_all.return_value = payrolls

    result = service.get_all_payroll()

    repository.get_all.assert_called_once()

    assert result == payrolls

def test_get_employee_payrolls():
    repository = MagicMock()
    service = PayrollService(repository)

    payrolls = [
        create_payroll(),
        create_payroll(),
    ]

    repository.get_by_employee_id.return_value = payrolls

    result = (service.get_employee_payroll(1))

    repository.get_by_employee_id.assert_called_once_with(1)

    assert result == payrolls


def test_delete_payroll():
    repository = MagicMock()
    service = PayrollService(repository)

    payroll = create_payroll()

    repository.get_by_id.return_value = payroll

    service.delete_payroll(1)

    repository.get_by_id.assert_called_once_with(1)
    repository.delete.assert_called_once_with(payroll)


def test_delete_payroll_not_found():
    repository = MagicMock()
    service = PayrollService(repository)

    repository.get_by_id.return_value = None

    with pytest.raises(ValueError, match="Payroll does not exist"):
        service.delete_payroll(999)

    repository.delete.assert_not_called()