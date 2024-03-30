# Ticket.py
#importing VisitorCategory from VisitorCategory
from VisitorCategory import VisitorCategory
# Class representing a ticket for museum events and admission
class Ticket:
    VAT_RATE = 0.05

    def __init__(self, event, visitor_category, event_price=None):
        """
        Initialize a ticket for a museum event.

        Arguments:
            event (str): The name of the event.
            visitor_category (VisitorCategory): The category of the visitor.
            event_price (float, optional): The base price of the event. Defaults to None.
        """
        self._event = event
        self._visitor_category = visitor_category
        self._event_price = event_price
        self._price = self.calculate_price()

    # Method to calculate the ticket price
    def calculate_price(self):
        """Calculate the ticket price based on visitor category and event type."""
        if self._event_price is not None:
            base_price = self._event_price
        else:
            base_price = 63 if self._event == "General Admission to museam without any event (no fee added)" else 73

        if self._visitor_category in [VisitorCategory.CHILD, VisitorCategory.STUDENT, VisitorCategory.SENIOR,
                                      VisitorCategory.TEACHER]:
            return 0
        elif self._visitor_category == VisitorCategory.GROUP:
            return base_price * (1 + Ticket.VAT_RATE) * 0.5  # Apply 50% discount for groups
        else:
            return base_price * (1 + Ticket.VAT_RATE)
