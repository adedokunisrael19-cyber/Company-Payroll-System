from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Payroll(Base):
    __tablename__ = "payrolls"

    id: Mapped[int] = mapped_column(
        primary_key=True
        
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id"),
        nullable=False
    )

    pay_period: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    basic_salary: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    allowances: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=Decimal("0.00"),
        nullable=False
    )

    deductions: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=Decimal("0.00"),
        nullable=False
    )

    net_salary: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    payment_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="PENDING",
        nullable=False
    )