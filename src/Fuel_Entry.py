class fuelEntry:
    def __init__(self, fuelLogDate, gallons, totalCost, odometer_Reading):
        self.fuelLogDate = fuelLogDate    
        self.gallons = gallons
        self.totalCost = totalCost
        self.odometer_Reading = odometer_Reading
       
       
        
    def __repr__(self):
        return f"Log: {(fuelEntry_list.index(self)+1)} \nGallons of Fuel: {self.gallons}\nTotal Cost of Fuel: {self.totalCost}\nOdometer Reading: {self.odometer_Reading}\n\n"
    
fuelEntry_list = []

def create_FuelEntry_List(FuelEntry):
    fuelEntry_desc_list = [FuelEntry]
    fuelEntry_list.append(FuelEntry)
    print(len(fuelEntry_list))
    return
