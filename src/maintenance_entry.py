# from vehicle import Vehicle
"""
Name: maintenance_entry.py
Authors: Michael Barthauer,
Date last updated: 9/29/2023
Description:
"""


class MaintenanceEntry:
    """Stores information relating to a specific maintenance check."""

    def __init__(self, vehicle, date, signature, costs, cost_labels, odometer=0):
        """Initializes MaintenanceEntry"""
        self.vehicle = vehicle  # Vehicle object reference
        self.date = date  # "YYYY-MM-DD" iso format, date maintenance occurred
        self.miles_as_of = odometer  # if not specified, this is set the same as vehicle's current odometer
        self.check_signed_by = signature  # who signed the check / paid for the maintenance

        # the following parallel tuples could be put in a dictionary instead
        self.check_entries = tuple(costs)  # tuple of costs enumerated in the bill
        # parallel tuple to check_entries, stores string labels for each cost ("parts", "labor", etc)
        self.check_categories = tuple(cost_labels)


        pass
