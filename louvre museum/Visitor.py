# Visitor.py
#importing Person class
from Person import Person
# Class representing a visitor, inherited from Person class
class Visitor(Person):
    """
    A class to represent a visitor, inherited from Person class.

    Inheritance:
    Visitor class inherits from the Person class.
    """

    def __init__(self, name, age, is_part_of_group):
        """Initialize a visitor with name, age, and group status."""
        super().__init__(name)
        self._age = age
        self._is_part_of_group = is_part_of_group
        self._ticket = None

    # Getter and setter methods for age and group status
    def get_age(self):
        """Get the age of the visitor."""
        return self._age

    def set_age(self, age):
        """Set the age of the visitor."""
        self._age = age

    def is_part_of_group(self):
        """Check if the visitor is part of a group."""
        return self._is_part_of_group

    def set_is_part_of_group(self, is_part_of_group):
        """Set whether the visitor is part of a group."""
        self._is_part_of_group = is_part_of_group

    # Method to purchase a ticket for the visitor
    def purchase_ticket(self, ticket):
        """Purchase a ticket for the visitor."""
        self._ticket = ticket
