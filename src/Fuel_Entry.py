class fuelEntry:
    def __init__(self, fuelLogDate, gallons, totalCost, odometer_Reading):
        self.fuelLogDate = fuelLogDate    
        self.gallons = gallons
        self.totalCost = totalCost
        self.odometer_Reading = odometer_Reading
       
       
        
    def FL(self):
        print("Gallons of Fuel:  " + self.gallons + "\nTotal Cost of Fuel: " + self.totalCost + "\nOdometer Reading: ", self.odometer_Reading)
       
       
if __name__ == "__main__":
    import datetime
    fuelLogDate  = datetime.date.today() #make an input
    gallons = float(input("How many gallons is in your car: "))
    totalCost = float(input("What is your total cost"))
    odometer_Reading = int(input("What is your odometer reading"))
    
    
    FLog = fuelEntry(gallons, totalCost, odometer_Reading)
print("Today's date is : ", fuelLogDate)   
FLog.FL()
