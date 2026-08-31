import unittest
from datetime import date

from app.database.database import SessionLocal
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.services.employee_service import EmployeeService


class TestEmployeeService(unittest.TestCase):

    def setUp(self):
        db_session = SessionLocal()
        repository = EmployeeRepository(db_session)
        self.service = EmployeeService(repository)

    def test_register_employee(self):
        employee = Employee(
            first_name="Taofeek",
            last_name="Kehinde",
            email="service1@gmail.com",
            position="Developer",
            base_salary=250000,
            hire_date=date(2026, 1, 25)
        )

        result = self.service.register_employee(employee)

        self.assertEqual(result.first_name, "Taofeek")

    def test_get_employee(self):
        employee = Employee(
            first_name="Ade",
            last_name="Olu",
            email="service2@gmail.com",
            position="Developer",
            base_salary=250000,
            hire_date=date(2026, 1, 25)
        )

        saved_employee = self.service.register_employee(employee)

        result = self.service.get_employee(saved_employee.id)

        self.assertEqual(result.first_name, "Ade")

    def test_get_all_employees(self):
        result = self.service.get_all_employees()

        self.assertIsInstance(result, list)

    def test_update_employee(self):
        employee = Employee(
            first_name="John",
            last_name="Doe",
            email="service3@gmail.com",
            position="Developer",
            base_salary=200000,
            hire_date=date(2026, 1, 25)
        )

        saved_employee = self.service.register_employee(employee)

        saved_employee.position = "Manager"

        result = self.service.update_employee(
            saved_employee.id,
            saved_employee
        )

        self.assertEqual(result.position, "Manager")

    def test_delete_employee(self):
        employee = Employee(
            first_name="Test",
            last_name="User",
            email="service4@gmail.com",
            position="Intern",
            base_salary=50000,
            hire_date=date(2026, 1, 25)
        )

        saved_employee = self.service.register_employee(employee)

        result = self.service.delete_employee(saved_employee.id)

        self.assertIsNone(
            self.service.get_employee(saved_employee.id)
        )


if __name__ == "__main__":
    unittest.main()