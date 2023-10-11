class fuelLog:
    def __init__(self, fuelLogDate, gallons, totalCost, odometer_Reading, miles_per_gallon, cost_per_mile, cost_per_gallon, log_creation, log_updated):
        self.fuelLogDate = fuelLogDate    
        self.gallons = gallons
        self.totalCost = totalCost
        self.odometer_Reading = odometer_Reading
        self.miles_per_gallon = miles_per_gallon
        self.cost_per_mile = cost_per_mile
        self.cost_per_gallon = cost_per_gallon
        self.log_creation = log_creation
        self.log_updated = log_updated
        
    def FL(self):
        print("Gallons of Fuel:  " + self.gallons + "\nTotal Cost of Fuel: " + self.totalCost + "\nOdometer Reading: ", self.odometer_Reading , "\nMiles per Gallon: " + self.miles_per_gallon + "\nCost per Mile: " + self.cost_per_mile + "\nCost per Gallon: ", self.cost_per_gallon , "\nThis Log was created on: " + self.log_creation + "\nThis log was updated on: ", self.log_updated)
       
       
if __name__ == "__main__":
    import datetime
    fuelLogDate  = datetime.date.today()
    gallons = float(input("How many gallons is in your car: "))
    totalCost = float(input("What is your total cost"))
    odometer_Reading = int(input("What is your odometer reading"))
    miles_per_gallon = float()
    cost_per_mile = float()
    cost_per_gallon =float()
    log_creation = 
    log_updated =
    
    FLog = fuelLog(gallons, totalCost, odometer_Reading, miles_per_gallon, cost_per_mile, cost_per_gallon, log_creation, log_updated)
print("Today's date is : ", fuelLogDate)   
FLog.FL()