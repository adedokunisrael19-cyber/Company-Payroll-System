import unittest
from datetime import date

from app.models.employee import Employee


class TestEmployeeModel(unittest.TestCase):

    def test_employee_creation(self):
        employee = Employee(
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
        self.assertEqual(employee.position, "Developer")
        self.assertEqual(employee.base_salary, 250000)
        self.assertEqual(employee.hire_date, date(2026, 1, 25))


if __name__ == "__main__":
    unittest.main()