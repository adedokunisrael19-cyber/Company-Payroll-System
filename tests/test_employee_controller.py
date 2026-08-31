import unittest
from datetime import date
from app.controllers.employee_controller import create_employee, delete_employee, update_employee
from app.controllers.employee_controller import get_employee
from app.controllers.employee_controller import list_employees
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate

class TestEmployeeController(unittest.TestCase):

    def test_create_employee(self):
        employee = EmployeeCreate(
            first_name="Taofeek",
            last_name="Kehinde",
            email="taofeek@gmail.com",
            position="Developer",
            base_salary=250000,
            hire_date=date(2026, 1, 25)
        )

        result = create_employee(employee)

        self.assertEqual(result.first_name, "Taofeek")

    def test_get_employee(self):
        result = get_employee(1)

        self.assertEqual(result.id, 1)

    def test_list_employees(self):
        result = list_employees()

        self.assertIsInstance(result, list)

    def test_update_employee(self):
        employee = EmployeeUpdate(
            position="Manager"
        )

        result = update_employee(1, employee)

        self.assertEqual(result.position, "Manager")

    def test_delete_employee(self):
        result = delete_employee(1)

        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()