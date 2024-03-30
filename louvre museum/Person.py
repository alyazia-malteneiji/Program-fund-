# Person.py

# Base class representing a person
class Person:
    """A class to represent a person."""

    def __init__(self, name):
        """Initialize a person with a name."""
        self._name = name

    def get_name(self):
        """Get the name of the person."""
        return self._name

    def set_name(self, name):
        """Set the name of the person."""
        self._name = name