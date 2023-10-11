class maintenanceEntry:
    def __init__(self, serviceDate, serviceName, serviceCost, serviceOdometerReading, serviceShopName):
        self.serviceDate = serviceDate    
        self.serviceName = serviceName
        self.serviceCost = serviceCost
        self.serviceOdometerReading = serviceOdometerReading
        self.serviceShopName = serviceShopName
        
    
    def rlog(self):
        print("Service Name: " + self.serviceName + "\nService Cost: ", self.serviceCost ,  "\nService Odometer Reading: ", self.serviceOdometerReading ,  "\nService Shop Name: " + self.serviceShopName)
       
       
if __name__ == "__main__":
    import datetime
    serviceDate  = datetime.date.today()
    serviceName = str(input("What is the name of the service you are getting? "))
    serviceCost = float(input("How much was the cost of your service? "))
    serviceOdometerReading = int(input("What is your service Odometer Reading? "))
    serviceShopName = str(input("What is the name of the shop that provided the service? "))
    mlog = maintenanceEntry(serviceDate, serviceName, serviceCost,serviceOdometerReading,serviceShopName)
print("Today's date is : ", serviceDate)
mlog.rlog()
