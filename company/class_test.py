from Manager_class import Manager
from Salesperson_class import Salesperson
from Cashier_class import Cashier


# Test Class
manager1 = Manager("John Smith", "123456789", "Married", "123 Street A", 5000, 1000)
salesperson1 = Salesperson("Alice Martin", "987654321", "Single", "456 Street B", 3000, 500, "Alan Walker")
cashier1 = Cashier("Pauline Dubois", "567890123", "Divorced", 2500, "789 Street C", "Edward")

# Display information for each employee
manager1.to_string()
print("\n")
salesperson1.to_string()
print("\n")
cashier1.to_string()