# Exhibition.py
#importing Location
from Location import Location
#importing random
import random
#importing date and time
from datetime import datetime, timedelta
# Class representing an exhibition
class Exhibition:
    """
    A class to represent an Exhibition.

    Aggregation Relationship:
    The Exhibition class is aggregated within the Museum class.
    """

    def __init__(self, name, start_date, end_date):
        """
        Initialize an exhibition with name, start date, and end date.

        Arguments:
            name (str): The name of the exhibition.
            start_date (datetime): The start date of the exhibition.
            end_date (datetime): The end date of the exhibition.
        """
        self._name = name
        self._location = random.choice(list(Location))
        self._start_date = start_date
        self._end_date = end_date

    # Getter methods for exhibition name, location, start date, and end date
    def get_name(self):
        """Get the name of the exhibition."""
        return self._name

    def get_location(self):
        """Get the location of the exhibition."""
        return self._location.name.replace('_', ' ').title()

    def get_start_date(self):
        """Get the start date of the exhibition."""
        return self._start_date

    def get_end_date(self):
        """Get the end date of the exhibition."""
        return self._end_date

    # Setter methods for exhibition name, location, start date, and end date
    def set_name(self, name):
        """Set the name of the exhibition."""
        self._name = name

    def set_location(self, location):
        """Set the location of the exhibition."""
        self._location = location

    def set_start_date(self, start_date):
        """Set the start date of the exhibition."""
        self._start_date = start_date

    def set_end_date(self, end_date):
        """Set the end date of the exhibition."""
        self._end_date = end_date
