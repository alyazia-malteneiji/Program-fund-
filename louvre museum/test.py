from enum import Enum
import random
from datetime import datetime, timedelta
from Person import Person
from VisitorCategory import VisitorCategory
from Visitor import Visitor
from Employee import Employee
from Artwork import Artwork
from Location import Location
from Exhibition import Exhibition
from Artwork import Artwork
from Ticket import Ticket
from Museum import Museum

# Function to create a visitor
def create_visitor():
    """
    Create a visitor based on user input.

    Returns:
        Visitor: A visitor object with provided details.
    """
    try:
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        is_part_of_group = input("Are you part of a group? (yes/no): ").lower() == 'yes'
        visitor = Visitor(name, age, is_part_of_group)
        return visitor
    except ValueError:
        print("Invalid input. Please enter a valid name and age.")
        return None


# Function to create an employee
def create_employee():
    """
    Create an employee based on user input.

    Returns:
        Employee: An employee object with provided details.
    """
    try:
        name = input("\nPlease enter your name: ")
        employee_id = input("Please enter your employee ID: ")
        employee = Employee(name, employee_id)
        return employee
    except ValueError:
        print("Invalid input. Please enter a valid name and employee ID.")
        return None


# Function to create an artwork and add it to the museum
def create_artwork(museum):
    """
    Create an artwork based on user input and add it to the museum's collection.

    Arguments:
        museum (Museum): The museum object to add the artwork to.
    """
    try:
        title = input("\nEnter artwork title: ")
        artist = input("Enter artist name: ")
        year = int(input("Enter year of creation: "))

        print("Choose the location for the artwork:")
        locations = list(Location)
        for index, location in enumerate(locations, start=1):
            print(f"{index}: {location.name.replace('_', ' ').title()}")

        location_choice = int(input("Enter your choice: "))
        location = locations[location_choice - 1]

        artwork = Artwork(title, artist, year, location)
        museum.add_artwork(artwork)
        print("Artwork added successfully.")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")
        return None


# Function to create exhibitions and add them to the museum
def create_exhibitions(museum):
    """
    Create exhibitions and add them to the museum's collection.

    Arguments:
        museum (Museum): The museum object to add the exhibitions to.
    """
    exhibition_names = ["Ancient Civilizations(extra 10 aed fee)", "Modern Art Gallery(extra 10 aed fee)", "Nature's Wonders(extra 10 aed fee)", "General Admission to museam without any event (no fee added)"]
    for name in exhibition_names:
        start_date = datetime.now() + timedelta(days=random.randint(1, 30))
        end_date = start_date + timedelta(days=random.randint(7, 30))
        exhibition = Exhibition(name, start_date, end_date)
        museum.add_exhibition(exhibition)


# Function for a visitor to purchase tickets
def purchase_tickets(visitor, museum):
    """
    Allow a visitor to purchase tickets for museum events.

   Arguments:
        visitor (Visitor): The visitor purchasing the ticket.
        museum (Museum): The museum object containing the events.
    """
    exhibitions = museum.get_exhibitions()
    if not exhibitions:
        print("Currently, there are no events available for ticket purchase.")
        return

    print("Available events:")
    for i, exhibition in enumerate(exhibitions, start=1):
        print(f"{i}. {exhibition.get_name()}")

    try:
        event_number = int(input("Enter the number of the event you want to attend: ")) - 1
        selected_exhibition = exhibitions[event_number]

        category_str = input("Enter your category (ADULT/CHILD/STUDENT/TEACHER/SENIOR/GROUP): ").upper()
        visitor_category = VisitorCategory[category_str]

        if visitor_category == VisitorCategory.GROUP:
            while True:
                try:
                    group_size = int(input("Enter the number of people in the group: "))
                    if group_size <= 0:
                        raise ValueError("Group size must be a positive integer.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number of people in the group.")

            ticket_price = 63 if selected_exhibition.get_name() == "General Admission to museam without any event (no fee added)" else 73
            total_price = ticket_price * group_size

            # Apply 50% discount for groups
            discounted_price = total_price * 0.5

            # Apply 5% VAT
            vat_amount = discounted_price * 0.05

            # Calculate the final total price with the discount and VAT
            final_price = discounted_price + vat_amount
        else:
            ticket = Ticket(selected_exhibition.get_name(), visitor_category)
            final_price = ticket.calculate_price()  # Corrected line

        print(
            f"\nTotal price for the ticket{'s' if visitor_category == VisitorCategory.GROUP else ''} is: {final_price:.2f} AED")
        print("Thank you for your purchase. Enjoy your visit and the wonders our museum has to offer!")
    except (ValueError, IndexError, KeyError):
        print("Invalid input. Please try again.")


# Function for employee actions within the museum
def employee_actions(employee, museum):
    """
    Perform actions based on employee's choice within the museum.

    Arguments:
        employee (Employee): The employee performing the actions.
        museum (Museum): The museum object to perform actions on.
    """
    while True:
        print(f"\nWelcome, {employee.get_name()}! What would you like to do today?")
        action = input("1: Add artwork\n2: Remove artwork\n3: Quit\nChoose an option: ")

        if action == "1":
            create_artwork(museum)
        elif action == "2":
            title = input("Enter the title of the artwork to remove: ")
            success = museum.remove_artwork_by_title(title)
            if success:
                print(f"Artwork '{title}' has been removed.")
            else:
                print(f"No artwork found with the title '{title}'.")
        elif action == "3":
            print("Exiting employee menu.")
            break
        else:
            print("Invalid option selected. Please try again.")


# Function to run the test case
def run_test_case():
    """Run the test case for the museum management system."""
    museum = Museum("The Louvre Museum")
    create_exhibitions(museum)

    print("Welcome to The Louvre Museum Management System")

    user_type = input("Are you a visitor or an employee? (v/e): ").lower()
    if user_type == "v":
        visitor = create_visitor()
        if visitor:
            print(f"\nWelcome, {visitor.get_name()}! What would you like to do today?")
            action = input("1: Purchase tickets\n")
            if action == "1":
                purchase_tickets(visitor, museum)
    elif user_type == "e":
        employee = create_employee()
        if employee:
            employee_actions(employee, museum)
        else:
            print("Invalid user type or invalid input. Exiting program.")


# Run the test case
run_test_case()
