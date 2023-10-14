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
        self.service_name = service_name
        self.service_date = service_date  # "YYYY-MM-DD" iso format, date maintenance occurred
        self.service_cost = service_cost
        self.odometer_reading = odometer_reading

        # the following parallel tuples could be put in a dictionary instead
        #self.check_entries = tuple(costs)  # tuple of costs enumerated in the bill
        # parallel tuple to check_entries, stores string labels for each cost ("parts", "labor", etc)
        #self.check_categories = tuple(cost_labels)

    #def get_costs_as_string(self):
    #    return "\n".join(f"{cost} - {label}" for cost, label in zip(self.check_entries, self.check_categories))

    def __repr__(self):
        return f"Log: {(maintenanceEntry_list.index(self)+1)}\nDate: {self.service_date}\nOdometer Reading: {self.odometer_reading}\nService Performed: {self.service_name}\nTotal Cost: {self.service_cost}\nShop: {self.service_shop}\n\n"

maintenanceEntry_list = []

def create_maintenanceEntry_List(MaintenanceEntry):
    maintenanceEntry_desc_list = [MaintenanceEntry]
    maintenanceEntry_list.append(MaintenanceEntry)
    print(len(maintenanceEntry_list))
    return