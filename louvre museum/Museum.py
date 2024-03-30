# Museum.py
#importing Artwork from Artwork class
from Artwork import Artwork
#importing Exhibition from Exhibition class
from Exhibition import Exhibition

# Class representing a Museum
class Museum:
    """
    A class to represent a Museum.

    Aggregation Relationship:
    The Museum class aggregates Artwork and Exhibition objects.
    """

    def __init__(self, name):
        """Initialize a museum with a name."""
        self._name = name
        self._artworks = []  # Aggregation relationship (Museum aggregates Artwork objects)
        self._exhibitions = []  # Aggregation relationship (Museum aggregates Exhibition objects)

    # Getter method for museum name
    def get_name(self):
        """Get the name of the museum."""
        return self._name

    # Method to add an artwork to the museum's collection
    def add_artwork(self, artwork):
        """Add an artwork to the museum's collection."""
        self._artworks.append(artwork)

    # Method to remove an artwork from the museum's collection
    def remove_artwork_by_title(self, title):
        """
        Remove an artwork from the museum's collection by title.

        Returns:
            bool: True if the artwork is removed successfully, False otherwise.
        """
        for artwork in self._artworks:
            if artwork.get_title() == title:
                self._artworks.remove(artwork)
                print(f"Artwork titled '{title}' has been removed.")
                return True
        print(f"No artwork found with the title '{title}'.")
        return False

    # Method to add an exhibition to the museum's collection
    def add_exhibition(self, exhibition):
        """Add an exhibition to the museum's collection."""
        self._exhibitions.append(exhibition)

    # Getter method to retrieve all exhibitions in the museum
    def get_exhibitions(self):
        """Get all exhibitions in the museum."""
        return self._exhibitions

    # Getter method to retrieve all artworks in the museum's collection
    def get_artworks(self):
        """Get all artworks in the museum's collection."""
        return self._artworks[:]
