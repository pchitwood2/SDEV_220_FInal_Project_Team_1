# from user.py import User
"""
Name: vehicle.py
Authors: Michael Barthauer,
Date last updated: 9/29/2023
Description: Defines class Vehicle which stores vehicle information.
"""


class Vehicle:
    miles_total = 0  # total number of miles
    miles_log = {}  # {"YYYY-MM-DD": <miles_driven>} for each day the vehicle is driven
    maintenance_log = []  # list of MaintenanceEntry instances
    pass
