"""
Name: vehicle.py
Authors: Michael Barthauer, Michael Coughlin
Date last updated: 10/14/2023
Description: Defines class Vehicle which stores vehicle information.
"""

#Vehicle Class
class Vehicle:
    def __init__(self, year, make, model, color, license_plate_number):
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.license_plate_number = license_plate_number

    #This produces a printable version of the class
    def __repr__(self):
        return f"{self.year} {self.make} {self.model}"

#This is the list containing the vehicles
vehicle_list = []

#This function moves the class data into the list
def create_vehicle_list(vehicle):
    vehicle_desc_list = [vehicle]
    vehicle_list.append(vehicle)
    print(len(vehicle_list))
    return


