from abc import ABCMeta, abstractmethod

# Abstract base class for employees
class Employee(metaclass=ABCMeta):
    _number_of_instances = 0  # Counter for tracking the number of employee instances

    # Constructor for the Employee class
    def __init__(self, name, social_security_number, marital_status, base_salary, address):
        Employee._number_of_instances += 1
        self._employee_id = Employee._number_of_instances  # Unique identifier for each employee
        self._name = name
        self._social_security_number = social_security_number
        self._marital_status = marital_status
        self._base_salary = base_salary
        self._address = address

    @property
    def get_name(self):
        return self._name

    @property
    def get_employee_id(self):
        return self._employee_id

    @property
    def get_social_security_number(self):
        return self._social_security_number

    @property
    def get_marital_status(self):
        return self._marital_status

    @property
    def get_address(self):
        return self._address

    @property
    def get_base_salary(self):
        return self._base_salary

    @abstractmethod
    def salary(self):
        pass  # Abstract method to be implemented by derived classes

    def equals(self, other):
        return isinstance(other, Employee) and self.get_employee_id == other.get_employee_id

    def to_string(self):
        print(f"Employee ID: {self.get_employee_id}")
        print(f"Name: {self.get_name}")
        print(f"Social Security Number: {self.get_social_security_number}")
        print(f"Marital Status: {self.get_marital_status}")
        print(f"Address: {self.get_address}")