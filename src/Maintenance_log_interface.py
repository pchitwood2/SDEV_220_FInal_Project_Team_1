"""Name: Maintenance_log_interface.py
Last updated: 10/14/2023
Authors: Justin Baeten, Peyton Chitwood, Michael Barthauer, Marc-Anthony Bradley, Michael Coughlin
Description: This is the GUI file for the Vstart application. It will take
various inputs to log data for vehicles."""
import tkinter.tix
import tkinter.ttk
from tkinter import *
from vehicle import *
from maintenance_entry import *
from Fuel_Entry import *

# master window setup
root = Tk()
root.title('Vehicle Maintenance Log')
root.geometry('1000x500')  # (width x height)
root.config(bg='skyblue')

# Vehicle information Frame
vehicle_frame = Frame(root, width=420, height=370)
vehicle_frame.place(x=280, y=20)

vehicle_header = Label(text='Vehicle Information ', font=24)  # Vehicle Information
vehicle_header.place(x=440, y=40)

year = Label(text='Year: ', font=18)  # Year vehicle was made
year.place(x=380, y=130)
year_entry = Entry(root, width=16)
year_entry.place(x=470, y=130)

make_of_vehicle = Label(text='Make: ', font=18)  # Make of vehicle
make_of_vehicle.place(x=380, y=170)
make_of_vehicle_entry = Entry(root, width=16)
make_of_vehicle_entry.place(x=470, y=170)

model_of_vehicle = Label(text='Model: ', font=18)  # Model of vehicle
model_of_vehicle.place(x=380, y=210)
model_of_vehicle_entry = Entry(root, width=16)
model_of_vehicle_entry.place(x=470, y=210)

vehicle_color = Label(text='Color: ', font=18)  # Model of vehicle
vehicle_color.place(x=380, y=250)
vehicle_color_entry = Entry(root, width=16)
vehicle_color_entry.place(x=470, y=250)

plate_number = Label(text='Plate Number: ', font=18)  # Model of vehicle
plate_number.place(x=340, y=290)
plate_number_entry = Entry(root, width=16)
plate_number_entry.place(x=470, y=290)


# function to clear values from user/vehicle form
def add_vehicle_button():
    #vehicle
    #clears entries, add vehicle to list
    if year_entry.get():
        if make_of_vehicle_entry.get():
            if model_of_vehicle_entry.get():
                if vehicle_color_entry.get():
                    if plate_number_entry.get():
                        vehicle = Vehicle(year_entry.get(), make_of_vehicle_entry.get(), model_of_vehicle_entry.get(),
                                          vehicle_color_entry.get(), plate_number_entry.get())
                        create_vehicle_list((vehicle))
                        year_entry.delete(0, END)
                        make_of_vehicle_entry.delete(0, END)
                        model_of_vehicle_entry.delete(0, END)
                        vehicle_color_entry.delete(0, END)
                        plate_number_entry.delete(0, END)
    else:
        return
    
    # Removes all Vehicle Entry frame Components
    vehicle_frame.destroy()
    vehicle_header.destroy()
    year.destroy()
    year_entry.destroy()
    make_of_vehicle.destroy()
    make_of_vehicle_entry.destroy()
    model_of_vehicle.destroy()
    model_of_vehicle_entry.destroy()
    vehicle_color.destroy()
    vehicle_color_entry.destroy()
    plate_number.destroy()
    plate_number_entry.destroy()
    add_vehicle.destroy()

    # Adds Maintenance and Fuel Entry Frames to Screen

    # Maintenance Frame
    maintenance_frame.place(x=40, y=20)

    maintenance_header.place(x=215, y=40)

    service_shop_name.place(x=100, y=90)
    service_shop_name_entry.place(x=210, y=90)

    service_name.place(x=100, y=125)
    service_name_entry.place(x=210, y=130)

    service_date.place(x=100, y=165)
    service_date_entry.place(x=210, y=170)

    service_cost.place(x=100, y=205)
    service_cost_entry.place(x=210, y=210)

    service_odometer_reading.place(x=60, y=245)
    service_odometer_reading_entry.place(x=210, y=250)

    submit_maintenanceEntry.place(x=215, y=330)

    # Fuel Frame
    fuel_log_frame.place(x=525, y=20)

    fuel_header.place(x=725, y=40)

    fuel_date.place(x=600, y=85)
    fuel_date_entry.place(x=710, y=90)

    fuel_cost.place(x=600, y=125)
    fuel_cost_entry.place(x=710, y=130)

    miles_per_gallon.place(x=600, y=165)
    miles_per_gallon_entry.place(x=710, y=170)

    fuel_odometer_reading.place(x=560, y=205)
    fuel_odometer_reading_entry.place(x=710, y=210)

    submit_fuelEntry.place(x=690, y=330)

    # Review Logs
    review_information.place(x=440, y=430)



# Maintenance log frame
maintenance_frame = Frame(root, width=450, height=370)
maintenance_frame.pack_forget()

maintenance_header = Label(text='Maintenance Log Entry', font=30)  # Maintenance Log Header
maintenance_header.pack_forget()


service_shop_name = Label(text='Service Shop: ', font=18)  # Service Shop Name
service_shop_name.pack_forget()
service_shop_name_entry = Entry(root, width=24)
service_shop_name_entry.pack_forget()

service_name = Label(text='Service Name: ', font=18)  # Service type
service_name.pack_forget()
service_name_entry = Entry(root, width=24)
service_name_entry.pack_forget()

service_date = Label(text='Service Date: ', font=18)  # Service date
service_date.pack_forget()
service_date_entry = Entry(root, width=24)
service_date_entry.pack_forget()

service_cost = Label(text='Service Cost: ', font=18)  # Service cost
service_cost.pack_forget()
service_cost_entry = Entry(root, width=24)
service_cost_entry.pack_forget()

service_odometer_reading = Label(text='Odometer Reading: ', font=18)  # Service Odometer Reading
service_odometer_reading.pack_forget()
service_odometer_reading_entry = Entry(root, width=24)
service_odometer_reading_entry.pack_forget()

# Frame for Fuel Log
fuel_log_frame = Frame(root, width=450, height=370)
fuel_log_frame.pack_forget()

fuel_header = Label(text='Fuel Log Entry', font=30)  # Fuel Log Header
fuel_header.pack_forget()


fuel_date = Label(text='Fuel Date: ', font=18)  # Fuel Date
fuel_date.pack_forget()
fuel_date_entry = Entry(root, width=18)
fuel_date_entry.pack_forget()

fuel_cost = Label(text='Fuel Cost: ', font=18)  # Fuel cost
fuel_cost.pack_forget()
fuel_cost_entry = Entry(root, width=18)
fuel_cost_entry.pack_forget()

miles_per_gallon = Label(text='Gallons: ', font=18)  # Miles Per gallon
miles_per_gallon.pack_forget()
miles_per_gallon_entry = Entry(root, width=18)
miles_per_gallon_entry.pack_forget()

fuel_odometer_reading = Label(text='Odometer Reading: ', font=18)  # Fuel odometer reading
fuel_odometer_reading.pack_forget()
fuel_odometer_reading_entry = Entry(root, width=18)
fuel_odometer_reading_entry.pack_forget()


# Function to create Review Log Window
def review_window():
    new_window = Toplevel()
    new_window.title("Vehicle Logs")
    new_window.geometry("1000x500")
    new_window.config(bg="skyblue")
    first_vehicle_frame = Frame(new_window, width="960", height="460")
    first_vehicle_frame.place(x=20, y=30)
    

    # Create a Vehicle Entry widget inside the frame
    vehicleEntry_View_Label = Label(first_vehicle_frame, text=f"Vehicle Logs for {''.join(str(vehicleEntries) for vehicleEntries in vehicle_list)}")
    vehicleEntry_View_Label.place(x=430, y=5)
    
    # Create a Fuel Entry widget inside the Frame
    fuelEntry_View_Label = Label(first_vehicle_frame, text="Fuel Entries")
    fuelEntry_View_Label.place(x=50, y=30)
    fuelEntry_View = Text(first_vehicle_frame, width=60, height=25)
    fuelEntry_View.place(x=50, y=50)
    fuelEntry_View.insert('1.0', f"{''.join(str(fuelEntries) for fuelEntries in fuelEntry_list)}")

    # Create a Maintenance Entry widget inside the Frame
    maintenanceEntry_View_Label = Label(first_vehicle_frame, text="Maintenance Entries")
    maintenanceEntry_View_Label.place(x=475, y=30)
    maintenanceEntry_View = Text(first_vehicle_frame, width=60, height=25)
    maintenanceEntry_View.place(x=475, y=50)
    maintenanceEntry_View.insert('1.0', f"{''.join(str(maintenanceEntries) for maintenanceEntries in maintenanceEntry_list)}")

    new_window.mainloop()


# Button to Review Logs
review_information = Button(root, text="Review Logs", bg='beige', font=12, command=review_window)
review_information.pack_forget()


# function for submit button for the Maintenance Entry
def submitMaintenanceEntry():
    maintenanceConfirmation_label = Label(root, text="Submission was Successful!", font=20)
    maintenanceConfirmation_label.place(x=205, y=365)
    #Maintenance Entry
    if service_shop_name_entry.get():
        if service_name_entry.get():
            if service_cost_entry.get():
                if service_odometer_reading_entry.get():
                    #insert maintenance hooks here
                    maintenance_entry = MaintenanceEntry(service_shop_name_entry.get(), service_name_entry.get(), service_date_entry.get(), service_cost_entry.get(), service_odometer_reading_entry.get())
                    create_maintenanceEntry_List((maintenance_entry))
                    service_shop_name_entry.delete(0, END)
                    service_cost_entry.delete(0, END)
                    service_name_entry.delete(0, END)
                    service_date_entry.delete(0, END)
                    service_odometer_reading_entry.delete(0, END)
    else:
        return
    root.after(2000, lambda: maintenanceConfirmation_label.destroy())


# Function for the submit button for the Fuel Entry
def submitFuelEntry():
    fuelConfirmation_label = Label(root, text="Submission was Successful!", font=20)
    fuelConfirmation_label.place(x=680, y=365)
    #Fuel Entry
    if fuel_date_entry.get():
        if fuel_cost_entry.get():
            if miles_per_gallon_entry.get():
                if fuel_odometer_reading_entry.get():
                    #insert fuel hooks here
                    fuel_entry = fuelEntry(fuel_date_entry.get(), miles_per_gallon_entry.get(), fuel_cost_entry.get(), fuel_odometer_reading_entry.get())
                    create_FuelEntry_List((fuel_entry))
                    fuel_date_entry.delete(0, END)
                    fuel_cost_entry.delete(0, END)
                    fuel_odometer_reading_entry.delete(0, END)
                    miles_per_gallon_entry.delete(0, END)

    else:
        return
    root.after(2000, lambda: fuelConfirmation_label.destroy())


# Submit Button that communicates to maintenance class
submit_maintenanceEntry = Button(root, text="Submit Entry", bg='lightgreen', font=12, command=submitMaintenanceEntry)
submit_maintenanceEntry.pack_forget()

# Submit Button that communicates to fuel class
submit_fuelEntry = Button(root, text="Submit Entry", bg='lightgreen', font=12, command=submitFuelEntry)
submit_fuelEntry.pack_forget()

# Button to Add New Entries to a different vehicle
add_vehicle = Button(root, text="Add Vehicle", bg='yellow', font=12, command=add_vehicle_button)
add_vehicle.place(x=440, y=330)




root.mainloop()
