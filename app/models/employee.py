from datetime import date

from sqlalchemy import Date, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    employee_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    hire_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    salary: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    payrolls = relationship(
        "Payroll",
        back_populates="employee"
    )