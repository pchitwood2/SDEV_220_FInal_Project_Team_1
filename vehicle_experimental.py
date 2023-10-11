class vehicle:
    def __init__(self, vehicle_info, vehicle_type, year, make, model, doors, roof, fuel_capacity, miles_driven, fuel):
        self.vehicle_info = vehicle_info
        self.vehicle_type = vehicle_type
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        self.fuel_capacity = fuel_capacity
        self.miles_driven = miles_driven
        self.fuel = fuel
        
    

    def Attributes(self):
        print("Vehicle Info " + self.vehicle_info + "\nVehicle_type: " + self.vehicle_type + "\nYear: ", self.year , "\nMake: " + self.make + "\nModel: " + self.model + "\nNumber of doors: ", self.doors , "\nType of roof: " + self.roof + "\nGallons of Fuel: ", self.fuel_capacity , "\nMiles Driven: ", self.miles_driven , "\nFuel Level: ", self.fuel)


if __name__ == "__main__":
    vehicle_type = str(input("Enter Vehicle Type: "))
    year = int(input("Enter year: "))
    make = str(input("Enter make: "))
    model = str(input("Enter model: "))
    doors = int(input("Enter number of doors: "))
    roof = str(input("Enter type of roof: "))
    fuel_capacity = float() 
    miles_driven = float
    fuel = float
    VehicleCL = vehicle("Is Below:", vehicle_type, year, make, model, doors, roof, fuel_capacity, miles_driven, fuel)
    VehicleCL.Attributes()