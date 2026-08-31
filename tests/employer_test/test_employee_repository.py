import unittest
from datetime import date

from app.database.database import SessionLocal
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository

class TestEmployeeRepository(unittest.TestCase):

    def setUp(self):
        self.db_session = SessionLocal()
        self.repository = EmployeeRepository(self.db_session)

    def test_save_employee(self):
        employee = Employee(
            first_name="Taofeek",
            last_name="Kehinde",
            email="taofeek@gmail.com.com",
            position="Developer",
            base_salary=250000,
            hire_date=date(2026, 1, 15)
        )

        result = self.repository.save(employee)

        self.assertEqual(result.first_name, "Taofeek")

    def test_find_employee_by_id(self):
        employee = Employee(
            first_name="Taofeek",
            last_name="Kehinde",
            email="taofeek2@gmail.com.com",
            position="Developer",
            base_salary=250000,
            hire_date=date(2026, 1, 15)
        )

        saved_employee = self.repository.save(employee)

        result = self.repository.find_by_id(saved_employee.id)

        self.assertEqual(result.email, "taofeek2@gmail.com")

    def test_find_employee_by_email(self):
        employee = Employee(
            first_name="Ade",
            last_name="Olu",
            email="ade@gmail.com",
            position="Manager",
            base_salary=300000,
            hire_date=date(2026, 1, 15)
        )

        self.repository.save(employee)

        result = self.repository.find_by_email("ade@gmail.com")

        self.assertEqual(result.first_name, "Ade")

    def test_get_all_employees(self):
        result = self.repository.get_all()

        self.assertIsInstance(result, list)

    def test_update_employee(self):
        employee = Employee(
            first_name="Elun",
            last_name="Musk",
            email="Elun@gmail.com",
            position="Developer",
            base_salary=200000,
            hire_date=date(2026, 1, 15)
        )

        saved_employee = self.repository.save(employee)

        saved_employee.position = "Manager"

        result = self.repository.update(saved_employee)

        self.assertEqual(result.position, "Manager")

    def test_delete_employee(self):
        employee = Employee(
            first_name="Test",
            last_name="User",
            email="delete@gmail.com",
            position="Intern",
            base_salary=50000,
            hire_date=date(2026, 1, 15)
        )

        saved_employee = self.repository.save(employee)

        self.repository.delete(saved_employee)

        result = self.repository.find_by_id(saved_employee.id)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()