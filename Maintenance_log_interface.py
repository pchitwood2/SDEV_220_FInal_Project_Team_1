from tkinter import *

# master window setup
root = Tk()
root.title('Vehicle Maintenance Log')
root.geometry('1200x840') # (width x height)
root.config(bg='skyblue')

# User/Vehicle information Frame
user_frame = Frame(root, width= 500, height=480) # User inforamtion
user_frame.place(x=20, y=20)
user_header = Label(text='User Info: ', font=24)
user_header.place(x=40, y=40)

first_name_label = Label(text='First Name: ', font=18) # First name label and entry
first_name_label.place(x=80, y=60)
first_name_entry = Entry(root, width=30)
first_name_entry.place(x=180, y=65)

last_name_label = Label(text='Last Name: ', font=18) # Last name label and entry
last_name_label.place(x=80, y=90)
last_name_entry = Entry(root, width=30)
last_name_entry.place(x=180, y=95)

section_divider =Label(text='--------------------------------------------------------------------------------------------')
section_divider.place(x=35, y=130)

vehicle_header = Label(text='Vehicle Info: ', font=24) # Vehicle Information
vehicle_header.place(x=40, y=160)
owner = Label(text='Owner: ', font=18) # Vehicle Owner
owner.place(x=80, y=180)
owner_entry = Entry(root, width=40)
owner_entry.place(x=180, y=185)

driver = Label(text='Driver: ', font=18) # Driver of the vehicle
driver.place(x=80, y=215)
driver_entry = Entry(root, width=40)
driver_entry.place(x=180, y=220)

vehicle_tipe = Label(text='Type: ', font=18) # Type of vehicle
vehicle_tipe.place(x=80, y=250)
vehicle_tipe_entry = Entry(root, width=20)
vehicle_tipe_entry.place(x=180, y=255)

year = Label(text='Year: ', font=18) # Year vehicle was made
year.place(x=80, y=285)
year_entry = Entry(root, width=10)
year_entry.place(x=180, y=290)

make_of_vehicle = Label(text='Make: ', font=18) # Make of vehicle
make_of_vehicle.place(x=80, y=320)
make_of_vehicle_entry = Entry(root, width=20)
make_of_vehicle_entry.place(x=180, y=325)

model_of_vehicle = Label(text='Model: ', font=18) # Model of vehicle
model_of_vehicle.place(x=80, y=355)
model_of_vehicle_entry = Entry(root, width=20)
model_of_vehicle_entry.place(x=180, y=360)

miles_since_last_maintenance = Label(text='Miles since last maintenance: ', font=18) # Miles since last maintenance
miles_since_last_maintenance.place(x=80, y=390)
miles_since_last_maintenance_entry = Entry(root, width=20)
miles_since_last_maintenance_entry.place(x=320, y=395)

time_since_last_maintenance = Label(text='Time since last maintenance: ', font=18) # Time since last maintenance
time_since_last_maintenance.place(x=80, y=425)
time_since_last_maintenance_entry = Entry(root, width=20)
time_since_last_maintenance_entry.place(x=320, y=430)

#User/Vehicle Info submit button
submit_info = Button(root, text="Submit", bg='lightgreen', font=12)
submit_info.place(x=320, y=460)

#Button to reveiw past User/Vehicle Info
review_information = Button(root, text="Review Information Logs", bg='beige', font=12)
review_information.place(x=40, y=460)

# Maintenance log of users vehicle
maintenance_frame = Frame(root, width=640, height=320)
maintenance_frame.place(x=540, y=20)

maintenance_header = Label(text='Maintenance Log', font=30) # Maintenance Log Header
maintenance_header.place(x=800, y=25)

service_shop_name = Label(text='Service Shop: ', font=18) # Service Shop Name
service_shop_name.place(x=560, y=60)
service_shop_name_entry = Entry(root, width=30)
service_shop_name_entry.place(x=670, y=65)

service_type = Label(text='Service Type: ', font=18) # Service type
service_type.place(x=870, y=60)
service_type_entry = Entry(root, width=30)
service_type_entry.place(x=970, y=65)

service_date = Label(text='Service Date: ', font=18) # Service date
service_date.place(x=870, y=100)
service_date_entry = Entry(root, width=30)
service_date_entry.place(x=970, y=105)

service_cost = Label(text='Service Cost: ', font=18) # Service cost
service_cost.place(x=560, y=100)
service_cost_entry = Entry(root, width=30)
service_cost_entry.place(x=670, y=105)

service_odometer_reading = Label(text='Service Odometer Reading: ', font=18) # Service Odometer Reading
service_odometer_reading.place(x=560, y=140)
service_odometer_reading_entry = Entry(root, width=30)
service_odometer_reading_entry.place(x=780, y=145)

maintenance_interval = Label(text='Maintenance Interval: ', font=18) # Maintenance Interval
maintenance_interval.place(x=560, y=180)
maintenance_interval_entry = Entry(root, width=30)
maintenance_interval_entry.place(x=780, y=185)

datae_log_created = Label(text='Date Log Created: ', font=18) # Maintenance Interval
datae_log_created.place(x=560, y=220)
datae_log_created_entry = Entry(root, width=30)
datae_log_created_entry.place(x=780, y=225)

date_log_updated = Label(text='Date Log Updated: ', font=18) # Maintenance Interval
date_log_updated.place(x=560, y=260)
date_log_updated_entry = Entry(root, width=30)
date_log_updated_entry.place(x=780, y=265)

# Button to review past maintenance logs
review_maintenance_log = Button(root, text="Review Maintenance Logs", bg='beige', font=12)
review_maintenance_log.place(x=560, y=300)

#Button to submit maintenance log
submit_maintenance = Button(root, text="Submit", bg='lightgreen', font=12)
submit_maintenance.place(x=780, y=300)

# Frame for Fuel Log
fuel_log_frame = Frame(root, width=640, height=400)
fuel_log_frame.place(x=540, y=420)

fuel_header = Label(text='Fuel Log', font=30) # Fuel Log Header
fuel_header.place(x=820, y=400+30)

fuel_added = Label(text='Fuel Added: ', font=18) # Fuel Added
fuel_added.place(x=660, y=430+30)
fuel_added_entry = Entry(root, width=30)
fuel_added_entry.place(x=770, y=435+30)

fuel_cost = Label(text='Fuel Cost: ', font=18) # Fuel cost
fuel_cost.place(x=660, y=470+30)
fuel_cost_entry = Entry(root, width=30)
fuel_cost_entry.place(x=770, y=475+30)

fuel_odometer_reading = Label(text='Fuel Odometer Reading: ', font=18) # Fuel odometer reading
fuel_odometer_reading.place(x=660, y=510+30)
fuel_odometer_reading_entry = Entry(root, width=20)
fuel_odometer_reading_entry.place(x=850, y=515+30)

miles_per_gallon = Label(text='Miles Per Gallon: ', font=18) # Miles Per gallon
miles_per_gallon.place(x=660, y=550+30)
miles_per_gallon_entry = Entry(root, width=15)
miles_per_gallon_entry.place(x=850, y=555+30)

cost_per_mile = Label(text='Cost Per Mile: ', font=18) # Cost Per Mile
cost_per_mile.place(x=660, y=590+30)
cost_per_mile_entry = Entry(root, width=15)
cost_per_mile_entry.place(x=850, y=595+30)

cost_per_gallon = Label(text='Cost Per Gallon: ', font=18) # Cost Per Gallon
cost_per_gallon.place(x=660, y=630+30)
cost_per_gallon_entry = Entry(root, width=15)
cost_per_gallon_entry.place(x=850, y=635+30)

fuel_log_created = Label(text='Fuel Log Created: ', font=18) # Fuel Log Created
fuel_log_created.place(x=660, y=670+30)
fuel_log_created_entry = Entry(root, width=15)
fuel_log_created_entry.place(x=850, y=675+30)

fuel_log_updated = Label(text='Fuel Log Updated: ', font=18) # Fuel Log Updated
fuel_log_updated.place(x=660, y=710+30)
fuel_log_updated_entry = Entry(root, width=15)
fuel_log_updated_entry.place(x=850, y=715+30)

#fuel submit button
submit_fuel = Button(root, text="Submit", bg='lightgreen', font=12)
submit_fuel.place(x=849, y=780)

#Button to reveiw past fuel logs
review_fuel_log = Button(root, text="Review Fuel Logs", bg='beige', font=12)
review_fuel_log.place(x=560, y=780)

#Update Maintenance Log
update_frame = Frame(root, width= 500, height=260) 
update_frame.place(x=20, y=560)
update_header = Label(text='Update Logs', font=24)
update_header.place(x=200, y=520+60)

clicked = StringVar() # Allows the drop down to activate
clicked.set("Select Log Type") # Sets a default value to the dropdown

maintenance_items = [
    "Serivce Shop",
    "Service Type", 
    "Service Date",
    "Service Odometer Reading",
    "Service_Cost",
    "Maintenance Interval",
    "Date Log Created",
    "Date Log Updated"
]
log_type_dropdown = OptionMenu(root, clicked, "User Info", "Vehicle Info", "Maintenance Log", "Fuel Log") # Log Options to tap into
log_type_dropdown.place(x=190, y=570+60)

field_dropdown = StringVar() # Field dropdown menu
field_dropdown.set("Select field type")
log_field = OptionMenu(root, field_dropdown, *maintenance_items)
log_field.place(x=190, y=610+60)

update_label = Label(root, text="Type Update Here: ") # Update entry box
update_label.place(x=70, y=655+60)
update_entry_box = Entry(root)
update_entry_box.place(x=190, y=660+60)
update_button = Button(root, text="Update", bg="darkgreen", fg="white", font=12)
update_button.place(x=210, y=690+60)


root.mainloop()