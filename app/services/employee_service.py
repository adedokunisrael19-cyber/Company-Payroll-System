from app.models.employee import Employee


class EmployeeService:

    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def register_employee(self, data):

        if data is None:
            raise ValueError("Employee is required")

        employee = Employee(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            position=data.position,
            base_salary=data.base_salary,
            hire_date=data.hire_date
        )

        return self.employee_repository.save(employee)

    def get_employee(self, id):

        if id <= 0:
            raise ValueError("Employee ID must be greater than 0")

        employee = self.employee_repository.find_by_id(id)

        if employee is None:
            raise ValueError("Employee not found")

        return employee

    def get_all_employees(self):
        return self.employee_repository.get_all()

    def update_employee(self, id, data):

        if id <= 0:
            raise ValueError("Employee ID must be greater than 0")

        employee = self.employee_repository.find_by_id(id)

        if employee is None:
            raise ValueError("Employee not found")

        if data is None:
            raise ValueError("Employee data is required")

        if data.first_name is not None:
            employee.first_name = data.first_name

        if data.last_name is not None:
            employee.last_name = data.last_name

        if data.email is not None:
            employee.email = data.email

        if data.position is not None:
            employee.position = data.position

        if data.base_salary is not None:
            employee.base_salary = data.base_salary

        if data.hire_date is not None:
            employee.hire_date = data.hire_date

        return self.employee_repository.update(employee)

    def delete_employee(self, id):

        if id <= 0:
            raise ValueError("Employee ID must be greater than 0")

        employee = self.employee_repository.find_by_id(id)

        if employee is None:
            raise ValueError("Employee not found")

        return self.employee_repository.delete(employee)