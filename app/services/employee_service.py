from app.models.employee import Employee

class EmployeeService:

    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def register_employee(self, data):
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
        return self.employee_repository.find_by_id(id)

    def get_all_employees(self):
        return self.employee_repository.get_all()

    def update_employee(self, id, data):
        employee = self.employee_repository.find_by_id(id)

        if employee is None:
            return None

        employee.first_name = data.first_name
        employee.last_name = data.last_name
        employee.email = data.email
        employee.position = data.position
        employee.base_salary = data.base_salary
        employee.hire_date = data.hire_date

        return self.employee_repository.update(employee)

    def delete_employee(self, id):
        employee = self.employee_repository.find_by_id(id)

        if employee is None:
            return None

        return self.employee_repository.delete(employee)