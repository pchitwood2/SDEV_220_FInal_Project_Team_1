from tkinter import *

# master window setup
root = Tk()
root.title('Vehicle Maintenance Log')
root.geometry('1200x780') # (width x height)
root.config(bg='skyblue')

# User/Vehicle information Frame
user_frame = Frame(root, width= 500, height=460) # User inforamtion
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

# Maintenance log of users vehicle
maintenance_frame = Frame(root, width=640, height=350)
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

# Frame for Fuel Log
fuel_log_frame = Frame(root, width=640, height=370)
fuel_log_frame.place(x=540, y=390)

fuel_header = Label(text='Fuel Log', font=30) # Fuel Log Header
fuel_header.place(x=820, y=400)

#Update Maintenance Log
update_frame = Frame(root, width= 500, height=260) 
update_frame.place(x=20, y=500)
update_header = Label(text='Update Logs', font=24)
update_header.place(x=200, y=520)

root.mainloop()