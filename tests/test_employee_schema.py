import unittest
from datetime import date
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate, EmployeeResponse

class TestEmployeeSchema(unittest.TestCase):

    def test_employee_create(self):
        employee = EmployeeCreate(
            first_name="Taofeek",
            last_name="Kehinde",
            email="taofeek@gmail.com",
            position="Developer",
            base_salary=250000,
            hire_date=date(2026, 1, 25)
        )

        self.assertEqual(employee.first_name, "Taofeek")
        self.assertEqual(employee.last_name, "Kehinde")
        self.assertEqual(employee.email, "taofeek@gmail.com")

    def test_employee_update(self):
        employee = EmployeeUpdate(
            position="Manager"
        )

        self.assertEqual(employee.position, "Manager")

    def test_employee_response(self):
        employee = EmployeeResponse(
            id=1,
            first_name="Taofeek",
            last_name="Kehinde",
            email="taofeek@gmail.com",
            position="Developer",
            base_salary=250000,
            hire_date=date(2026, 1, 25)
        )

        self.assertEqual(employee.id, 1)
        self.assertEqual(employee.first_name, "Taofeek")


if __name__ == "__main__":
    unittest.main()