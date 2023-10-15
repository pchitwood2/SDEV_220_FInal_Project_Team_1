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
    def __init__(self, service_shop, service_name, service_date, service_cost, odometer_reading):
        """Initializes MaintenanceEntry"""
        self.service_shop = service_shop  # name of the shop that supplied the maintenance
        self.service_name = service_name  # Name of the service provided
        self.service_date = service_date  # "YYYY-MM-DD" iso format, date maintenance occurred
        self.service_cost = service_cost  # Total cost of service
        self.odometer_reading = odometer_reading  # Reading of odometer at time of service

    # How maintenance entry objects are represented as strings
    def __repr__(self):
        return f"Log: {(maintenanceEntry_list.index(self)+1)}\nDate: {self.service_date}\nOdometer Reading: {self.odometer_reading}\nService Performed: {self.service_name}\nTotal Cost: {self.service_cost}\nShop: {self.service_shop}\n\n"

# Creates list where maintenance entry objects are added to
maintenanceEntry_list = []

# Initialized list and adds new objects to list
def create_maintenanceEntry_List(MaintenanceEntry):
    maintenanceEntry_desc_list = [MaintenanceEntry]
    maintenanceEntry_list.append(MaintenanceEntry)
    print(len(maintenanceEntry_list))
    return
