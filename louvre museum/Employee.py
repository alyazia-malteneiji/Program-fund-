# Employee.py
#importing Person class
from Person import Person
# Class representing an employee, inherited from Person class
class Employee(Person):
    """
    A class to represent an employee, inherited from Person class.

    Inheritance:
    Employee class inherits from the Person class.
    """

    def __init__(self, name, employee_id):
        """Initialize an employee with name and employee ID."""
        super().__init__(name)
        self._employee_id = employee_id

    # Getter and setter methods for employee ID
    def get_employee_id(self):
        """Get the employee ID."""
        return self._employee_id

    def set_employee_id(self, employee_id):
        """Set the employee ID."""
        self._employee_id = employee_id
