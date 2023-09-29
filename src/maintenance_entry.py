# from vehicle import Vehicle
"""
Name: maintenance_entry.py
Authors: Michael Barthauer,
Date last updated: 9/29/2023
Description:
"""


class MaintenanceEntry:
    """Stores information relating to a specific maintenance check."""
    def __init__(self, vehicle, date, odometer=0):
        self.vehicle = vehicle  # Vehicle object reference
        self.date = date  # "YYYY-MM-DD" iso format, date maintenance occurred
        self.miles_as_of = odometer
        pass
