from Employee_class import Employee

# Salesperson class, another derived class from Employee
class Salesperson(Employee):
    def __init__(self, name, social_security_number, marital_status, address, base_salary, commission, supervisor):
        super().__init__(name, social_security_number, marital_status, base_salary, address)
        self.__commission = commission  # Private attribute for the sales commission
        self.__supervisor = supervisor  # Private attribute for the supervisor

    @property
    def get_sales(self):
        return self.__commission

    @property
    def get_supervisor(self):
        return self.__supervisor

    def salary(self):
        return super().get_base_salary + self.get_sales  # Calculate salary including sales commission

    def to_string(self):
        super().to_string()
        print(f"Salary: {self.salary()}")
        print(f"Commission: {self.get_sales}")
        print(f"Supervisor: {self.get_supervisor}")