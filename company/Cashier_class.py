from Employee_class import Employee

# Cashier class, another derived class from Employee
class Cashier(Employee):
    def __init__(self, name, social_security_number, marital_status, base_salary, address, supervisor):
        super().__init__(name, social_security_number, marital_status, base_salary, address)
        self.__supervisor = supervisor  # Private attribute for the supervisor

    @property
    def get_supervisor(self):
        return self.__supervisor

    def salary(self):
        return super().get_base_salary  # Cashiers have no additional components in their salary

    def to_string(self):
        super().to_string()
        print(f"Salary: {self.salary()}")
        print(f"Supervisor: {self.get_supervisor}")