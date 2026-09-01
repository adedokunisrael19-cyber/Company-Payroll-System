from decimal import Decimal
from unittest.mock import MagicMock

from app.models.payroll import Payroll
from app.repositories.payroll import PayrollRepository


def create_payroll():
    return Payroll(
        employee_id=1,
        pay_period="August 2026",
        basic_salary=Decimal("500000.00"),
        allowances=Decimal("50000.00"),
        deductions=Decimal("20000.00"),
        net_salary=Decimal("530000.00"),
        status="PENDING"
    )

def test_create_payroll():
    db = MagicMock()
    repository = PayrollRepository(db)

    payroll = create_payroll()

    result = repository.create(payroll)

    db.add.assert_called_once_with(payroll)
    db.commit.assert_called_once_with()
    db.refresh.assert_called_once_with(payroll)

    assert result is payroll


def test_get_payroll_id():
    db = MagicMock()
    repository = PayrollRepository(db)
    payroll = create_payroll()

    db.query.return_value.filter.return_value.first.return_value = payroll

    result = repository.get_by_id(1)

    result == payroll

    db.query.assert_called_once_with(Payroll)

def test_get_all_payrolls():
    db = MagicMock()
    repository = PayrollRepository(db)

    payrolls = [create_payroll(), create_payroll(), create_payroll()]

    db.query.return_value.all.return_value = payrolls

    result = repository.get_all()


    assert result == payrolls
    db.query.assert_called_once_with(Payroll)


def test_get_payrolls_by_employee_id():
    db = MagicMock()
    repository = PayrollRepository(db)

    payrolls = [
        create_payroll(),
        create_payroll(),
    ]

    db.query.return_value.filter.return_value.all.return_value = payrolls

    result = repository.get_by_employee_id(1)

    assert result == payrolls

    db.query.assert_called_once_with(Payroll)

def test_update_payroll():
    db = MagicMock()
    repository = PayrollRepository(db)

    payroll = create_payroll()

    result = repository.update(payroll)

    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(payroll)

    assert result == payroll


def test_delete_payroll():
    db = MagicMock()
    repository = PayrollRepository(db)

    payroll = create_payroll()
    result = repository.delete(1)

    assert result is None