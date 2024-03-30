# Artwork.py
#importing Enum
from enum import Enum
#importing Loction Enum
from Location import Location
# Class representing an artwork
class Artwork:
    """
    A class to represent an Artwork.

    Composition:
    Artwork class is composed within the Museum class, as it's added to the museum's collection.
    """

    def __init__(self, title, artist, year, location):
        """Initialize an artwork with title, artist, year, and location."""
        self._title = title
        self._artist = artist
        self._year = year
        self._location = location

    # Getter and setter methods for title, artist, year, and location
    def get_title(self):
        """Get the title of the artwork."""
        return self._title

    def get_artist(self):
        """Get the artist of the artwork."""
        return self._artist

    def get_year(self):
        """Get the year of creation of the artwork."""
        return self._year

    def get_location(self):
        """Get the location of the artwork."""
        return self._location.value

    def set_title(self, title):
        """Set the title of the artwork."""
        self._title = title

    def set_artist(self, artist):
        """Set the artist of the artwork."""
        self._artist = artist

    def set_year(self, year):
        """Set the year of creation of the artwork."""
        self._year = year

    def set_location(self, location):
        """Set the location of the artwork."""
        if isinstance(location, Location):
            self._location = location
        else:
            raise ValueError("Invalid location")
