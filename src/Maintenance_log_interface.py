import tkinter.tix
import tkinter.ttk
from tkinter import *
from vehicle import *

# master window setup
root = Tk()
root.title('Vehicle Maintenance Log')
root.geometry('1470x540')  # (width x height)
root.config(bg='skyblue')


def select_dropdown():
    selection = dropdown.current()
    if selection == 0:
        year_entry.config(state="normal")
        make_of_vehicle_entry.config(state="normal")
        model_of_vehicle_entry.config(state="normal")
        vehicle_color_entry.config(state="normal")
        plate_number_entry.config(state="normal")
        add_vehicle.config(state="normal")
    else:
        year_entry.delete(0, END)
        make_of_vehicle_entry.delete(0, END)
        model_of_vehicle_entry.delete(0, END)
        vehicle_color_entry.delete(0, END)
        plate_number_entry.delete(0, END)
        year_entry.config(state="disabled")
        make_of_vehicle_entry.config(state="disabled")
        model_of_vehicle_entry.config(state="disabled")
        vehicle_color_entry.config(state="disabled")
        plate_number_entry.config(state="disabled")
        add_vehicle.config(state="disabled")


# Vehicle information Frame
vehicle_frame = Frame(root, width=450, height=340)
vehicle_frame.place(x=30, y=20)

vehicle_header = Label(text='Vehicle Information ', font=24)  # Vehicle Information
vehicle_header.place(x=210, y=40)

divider_one = Label(text="--------------------------------------------------------------------------")
divider_one.place(x=80, y=60)

dropdown = tkinter.ttk.Combobox(root, values=vehicle_list, width=30, state="readonly")
dropdown.place(x=200, y=90)
dropdown.current(0)
dropdown.bind("<<ComboboxSelected>>",lambda event: select_dropdown())

year = Label(text='Year: ', font=18)  # Year vehicle was made
year.place(x=200, y=130)
year_entry = Entry(root, width=10)
year_entry.place(x=280, y=130)

make_of_vehicle = Label(text='Make: ', font=18)  # Make of vehicle
make_of_vehicle.place(x=200, y=170)
make_of_vehicle_entry = Entry(root, width=20)
make_of_vehicle_entry.place(x=280, y=170)

model_of_vehicle = Label(text='Model: ', font=18)  # Model of vehicle
model_of_vehicle.place(x=200, y=210)
model_of_vehicle_entry = Entry(root, width=20)
model_of_vehicle_entry.place(x=280, y=210)

vehicle_color = Label(text='Color: ', font=18)  # Model of vehicle
vehicle_color.place(x=200, y=250)
vehicle_color_entry = Entry(root, width=20)
vehicle_color_entry.place(x=280, y=250)

plate_number = Label(text='Plate Number: ', font=18)  # Model of vehicle
plate_number.place(x=143, y=290)
plate_number_entry = Entry(root, width=20)
plate_number_entry.place(x=280, y=290)


# function to clear values from user/vehicle form
def user_info_reset():
    if year_entry.get():
        if make_of_vehicle_entry.get():
            if model_of_vehicle_entry.get():
                if vehicle_color_entry.get():
                    if plate_number_entry.get():
                        vehicle = Vehicle(year_entry.get(), make_of_vehicle_entry.get(), model_of_vehicle_entry.get(),
                                          vehicle_color_entry.get(), plate_number_entry.get())
                        create_vehicle_list(str(vehicle))
                        dropdown.config(values=vehicle_list)
                        year_entry.delete(0, END)
                        make_of_vehicle_entry.delete(0, END)
                        model_of_vehicle_entry.delete(0, END)
                        vehicle_color_entry.delete(0, END)
                        plate_number_entry.delete(0, END)

    elif service_shop_name_entry.get():
        if service_name_entry.get():
            if service_cost_entry.get():
                if service_odometer_reading_entry.get():
                    #insert maintenance hooks here
                    service_shop_name_entry.delete(0, END)
                    service_cost_entry.delete(0, END)
                    service_name_entry.delete(0, END)
                    service_date_entry.delete(0, END)
                    service_odometer_reading_entry.delete(0, END)

    elif fuel_date_entry.get():
        if fuel_cost_entry.get():
            if miles_per_gallon_entry.get():
                if fuel_odometer_reading_entry.get():
                    #insert fuel hooks here
                    fuel_date_entry.delete(0, END)
                    fuel_cost_entry.delete(0, END)
                    fuel_odometer_reading_entry.delete(0, END)
                    miles_per_gallon_entry.delete(0, END)

    else:
        return


# Maintenance log frame
maintenance_frame = Frame(root, width=450, height=340)
maintenance_frame.place(x=510, y=20)

maintenance_header = Label(text='Maintenance Log', font=30)  # Maintenance Log Header
maintenance_header.place(x=670, y=40)

divider_two = Label(text="--------------------------------------------------------------------------")
divider_two.place(x=545, y=60)

service_shop_name = Label(text='Service Shop: ', font=18)  # Service Shop Name
service_shop_name.place(x=560, y=85)
service_shop_name_entry = Entry(root, width=30)
service_shop_name_entry.place(x=670, y=90)

service_name = Label(text='Service Name: ', font=18)  # Service type
service_name.place(x=560, y=125)
service_name_entry = Entry(root, width=30)
service_name_entry.place(x=670, y=130)

service_date = Label(text='Service Date: ', font=18)  # Service date
service_date.place(x=560, y=165)
service_date_entry = Entry(root, width=30)
service_date_entry.place(x=670, y=170)

service_cost = Label(text='Service Cost: ', font=18)  # Service cost
service_cost.place(x=560, y=205)
service_cost_entry = Entry(root, width=30)
service_cost_entry.place(x=670, y=210)

service_odometer_reading = Label(text='Odometer Reading: ', font=18)  # Service Odometer Reading
service_odometer_reading.place(x=520, y=245)
service_odometer_reading_entry = Entry(root, width=30)
service_odometer_reading_entry.place(x=670, y=250)

# Frame for Fuel Log
fuel_log_frame = Frame(root, width=450, height=340)
fuel_log_frame.place(x=990, y=20)

fuel_header = Label(text='Fuel Log', font=30)  # Fuel Log Header
fuel_header.place(x=1180, y=40)

divider_three = Label(text="--------------------------------------------------------------------------")
divider_three.place(x=1025, y=60)

fuel_date = Label(text='Fuel Date: ', font=18)  # Fuel Date
fuel_date.place(x=1080, y=85)
fuel_date_entry = Entry(root, width=30)
fuel_date_entry.place(x=1180, y=90)

fuel_cost = Label(text='Fuel Cost: ', font=18)  # Fuel cost
fuel_cost.place(x=1080, y=125)
fuel_cost_entry = Entry(root, width=30)
fuel_cost_entry.place(x=1180, y=130)

miles_per_gallon = Label(text='Miles Per Gallon: ', font=18)  # Miles Per gallon
miles_per_gallon.place(x=1034, y=165)
miles_per_gallon_entry = Entry(root, width=15)
miles_per_gallon_entry.place(x=1180, y=170)

fuel_odometer_reading = Label(text='Odometer Reading: ', font=18)  # Fuel odometer reading
fuel_odometer_reading.place(x=1018, y=205)
fuel_odometer_reading_entry = Entry(root, width=20)
fuel_odometer_reading_entry.place(x=1180, y=210)


# Function to create Review Log Window
def review_window():
    new_window = Toplevel()
    new_window.title("Vehicle Logs")
    new_window.geometry("1000x500")
    new_window.config(bg="skyblue")
    first_vehicle_frame = Frame(new_window, width="960", height="460")
    first_vehicle_frame.place(x=20, y=20)


# Button to Review Logs
review_information = Button(root, text="Review Logs", bg='beige', font=12, command=review_window)
review_information.place(x=680, y=470)


# function for submit button
def show():
    confirmation_label = Label(root, text="Submission was Successful!", font=20, bg="skyblue")
    confirmation_label.place(x=770, y=385)


# Submit Button that communicates to classes
submit_vehicle_info = Button(root, text="Submit", bg='lightgreen', font=12, command=show)
submit_vehicle_info.place(x=700, y=380)

# Button to Add New Entries to a different vehicle
add_vehicle = Button(root, text="Add Vehicle", bg='yellow', font=12, command=user_info_reset)
add_vehicle.place(x=680, y=425)

root.mainloop()