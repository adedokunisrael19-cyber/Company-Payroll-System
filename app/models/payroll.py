from datetime import date

from sqlalchemy import Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Payroll(Base):
    __tablename__ = "payrolls"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id"),
        nullable=False
    )

    pay_period: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    gross_salary: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    total_deductions: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    net_salary: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    payment_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    employee = relationship(
        "Employee",
        back_populates="payrolls"
    )