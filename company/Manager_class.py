from Employee_class import Employee

# Manager class, a derived class from Employee
class Manager(Employee):
    def __init__(self, name, social_security_number, marital_status, address, base_salary, risk_bonus):
        super().__init__(name, social_security_number, marital_status, base_salary, address)
        self.__risk_bonus = risk_bonus  # Private attribute for the risk bonus

    def salary(self):
        return super().get_base_salary + self.get_risk_bonus  # Calculate salary including risk bonus

    @property
    def get_risk_bonus(self):
        return self.__risk_bonus

    @get_risk_bonus.setter
    def set_risk_bonus(self, ratio):
        if not isinstance(ratio, float):
            raise ValueError("The risk bonus must be a value between 0 and 1")

    def to_string(self):
        super().to_string()
        print(f"Salary: {self.salary()}")
        print(f"Risk Bonus: {self.get_risk_bonus}")