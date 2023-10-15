"""
Name: fuelEntry.py
Authors: Peyton Chitwood
Date last updated: 10/14/2023
Description: Defines class fuelEntry which stores fuel entry information.
"""

class fuelEntry:
    # Initializes Fuel Entry Class
    def __init__(self, fuelLogDate, gallons, totalCost, odometer_Reading):
        self.fuelLogDate = fuelLogDate    # The date of the fuel entry
        self.gallons = gallons    # Amount of gallons input
        self.totalCost = totalCost    # Total cost of fuel
        self.odometer_Reading = odometer_Reading    # Odometer Reading at purchase of fuel
       
       
    # How Fuel Entry Object is represented as a string    
    def __repr__(self):
        return f"Log: {(fuelEntry_list.index(self)+1)} \nGallons of Fuel: {self.gallons}\nTotal Cost of Fuel: {self.totalCost}\nOdometer Reading: {self.odometer_Reading}\n\n"

# List where Fuel Entry objects are stored
fuelEntry_list = []

# Function that initializes and adds newly created Fuel Entry objects to list
def create_FuelEntry_List(FuelEntry):
    fuelEntry_desc_list = [FuelEntry]
    fuelEntry_list.append(FuelEntry)
    print(len(fuelEntry_list))
    return
