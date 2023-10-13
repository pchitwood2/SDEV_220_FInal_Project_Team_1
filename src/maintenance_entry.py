# from vehicle import Vehicle
"""
Name: maintenance_entry.py
Authors: Michael Barthauer,
Date last updated: 10/13/2023
Description:
Defines a class for storing information representing a vehicle maintenance receipt.
Stores information such as the name of the vehicle shop, the costs, who signed the check, etc.
"""


class MaintenanceEntry:
    """Stores information relating to a specific maintenance check."""

    def __init__(self, shop_name, date, signature, costs, cost_labels, odometer):
        """Initializes MaintenanceEntry"""
        self.shop = shop_name  # name of the shop that supplied the maintenance
        self.date = date  # "YYYY-MM-DD" iso format, date maintenance occurred
        self.miles_as_of = odometer  # if not specified, this is set the same as vehicle's current odometer
        self.check_signed_by = signature  # who signed the check / paid for the maintenance

        # the following parallel tuples could be put in a dictionary instead
        self.check_entries = tuple(costs)  # tuple of costs enumerated in the bill
        # parallel tuple to check_entries, stores string labels for each cost ("parts", "labor", etc)
        self.check_categories = tuple(cost_labels)

    def get_costs_as_string(self):
        return "\n".join(f"{cost} - {label}" for cost, label in zip(self.check_entries, self.check_categories))

    def __repr__(self):
        return f"Date: {self.date}\nOdometer: {self.miles_as_of}\nCosts:{self.get_costs_as_string()}\nSigned by: {self.check_signed_by}"
