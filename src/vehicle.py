# from user.py import User
"""
Name: vehicle.py
Authors: Michael Barthauer, Michael Coughlin
Date last updated: 9/29/2023
Description: Defines class Vehicle which stores vehicle information.
"""


class Vehicle:
    def __init__(self, year, make, model, color, license_plate_number):
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.license_plate_number = license_plate_number

    """miles_total = 0  # total number of miles
    miles_log = {}  # {"YYYY-MM-DD": <miles_driven>} for each day the vehicle is driven
    maintenance_log = []  # list of MaintenanceEntry instances"""

    def __repr__(self):
        return f"{self.year} {self.make} {self.model}"


vehicle_list = []


def create_vehicle_list(vehicle):
    vehicle_desc_list = [vehicle]
    vehicle_list.append(vehicle)
    print(len(vehicle_list))
    return


