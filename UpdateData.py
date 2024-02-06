import tkinter as tk
from tkinter import ttk
import datetime
import pyrebase
import os
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox

def open_file1():
    os.system('python AdminHome.py')

# initialize Firebase
firebaseConfig = {
    "apiKey": "AIzaSyAhZ07NWcNM74HDWGVbeeN5nGGauQ2k-9Y",
    "authDomain": "facedetectiondatabase-7fe17.firebaseapp.com",
    "databaseURL": "https://facedetectiondatabase-7fe17-default-rtdb.firebaseio.com",
    "projectId": "facedetectiondatabase-7fe17",
    "storageBucket": "facedetectiondatabase-7fe17.appspot.com",
    "messagingSenderId": "906725895779",
    "appId": "1:906725895779:web:54743167bd7022f67fd256",
    "measurementId": "G-NB5XJGD085"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

window = tk.Tk()
window.title("Update Data to Firebase")

# load the background image and resize it
image = Image.open("build1.jpg")
image = image.resize((1920, 1080), Image.ANTIALIAS)

# create a PhotoImage object from the image file
photo = ImageTk.PhotoImage(image)

# create a label widget for the background image and place it behind all other widgets
background_label = tk.Label(window, image=photo, compound="center")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

name_label = tk.Label(window, text="Titan Property Management", bg="#ffffff", fg="#2b34d9", font=("Castellar", 24, "bold"))
name_label.grid(pady=20, row=0, column=15)

title_label = tk.Label(window, text=" Update Employee Data", width=20, height=3, bg="#ffffff", fg="#9040c2", font=("Gabriola", 21, "bold"))
title_label.grid(row=1, column=5)

# function to get current date and time
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d  %H:%M:%S")
    return current_time


id_label = tk.Label(window, text="ID", width=10, height=1, bg="#ffffff", font=("Gabriola", 16,"bold"))
id_entry = tk.Entry(window, font=("SimSun", 16))
id_label.grid(row=2, column=14)
id_entry.grid(row=2, column=15)

depart_label = tk.Label(window, text="Department", width=15, height=1, bg="#ffffff", font=("Gabriola", 16,"bold"))
depart_entry = tk.Entry(window)
depart_label.grid(row=3, column=14)
# create a dropdown button for the "Standing" field
depart_options = ["Carpet washing", "Vacuuming",  "Painting", "Plumbing", "Deep cleaning", "Electrical work", "Civil work", "Brass Polishing"]
depart_var = tk.StringVar(value=depart_options[0])
depart_dropdown = ttk.Combobox(window, textvariable=depart_var, values=depart_options, state="readonly", font=("SimSun", 16))
depart_dropdown.grid(row=3, column=15)

year_label = tk.Label(window, text="Joined_year", width=15, height=1, bg="#ffffff", font=("Gabriola", 16,"bold"))
year_entry = tk.Entry(window, font=("SimSun", 16))
year_label.grid(row=4, column=14)
year_entry.grid(row=4, column=15)

lastatt_label = tk.Label(window, text="Last Attendance", width=15, height=1, bg="#ffffff", font=("Gabriola", 16,"bold"))
lastatt_entry = tk.Entry(window, font=("SimSun", 16))
lastatt_entry.insert(0, get_current_time()) # set default value to current date and time
lastatt_label.grid(row=5, column=14)
lastatt_entry.grid(row=5, column=15)

name_label = tk.Label(window, text="Name", width=15, height=1, bg="#ffffff", font=("Gabriola", 16,"bold"))
name_entry = tk.Entry(window, font=("SimSun", 16))
name_label.grid(row=6, column=14)
name_entry.grid(row=6, column=15)

standing_label = tk.Label(window, text="Standing", width=15, height=1, bg="#ffffff", font=("Gabriola", 16,"bold"))
standing_entry = tk.Entry(window)
standing_label.grid(row=7, column=14)
# create a dropdown button for the "Standing" field
standing_options = ["Excellent", "Good", "Average", "Poor"]
standing_var = tk.StringVar(value=standing_options[0])
standing_dropdown = ttk.Combobox(window, textvariable=standing_var, values=standing_options, state="readonly", font=("SimSun", 16))
standing_dropdown.grid(row=7, column=15)


totalatt_label = tk.Label(window, text="Total Attendance", width=15, height=1, bg="#d9cc96", font=("Gabriola", 16,"bold"))
totalatt_entry = tk.Entry(window, font=("SimSun", 16))
totalatt_entry.insert(0, '0')
totalatt_label.grid(row=8, column=14)
totalatt_entry.grid(row=8, column=15)



# set the size of the window
window.geometry("1920x1080")

window.configure(bg="#934ae2")

# function to insert data into Firebase
def update_data():
    data = {
        "Id": id_entry.get(),
        "department": depart_var.get(),
        "joined_year": int(year_entry.get()),
        "last_attendance_time": lastatt_entry.get(),
        "name": name_entry.get(),
        "standing": standing_var.get(),
        "total_attendance": int(totalatt_entry.get())
    }
    messagebox.showinfo("Success", "Data has been Updated successfully!")
    db.child("Employees").child(id_entry.get()).update(data)
    id_entry.delete(0, tk.END)
    depart_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    lastatt_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    standing_entry.delete(0, tk.END)
    totalatt_entry.delete(0, tk.END)
    totalatt_entry.insert(0, '1')
    open_file1()


# create a button to insert data into Firebase
submit_button = tk.Button(window, text="Update", command=update_data,  bg="#cfc080", fg="white", padx=10, pady=5, font=("Gill Sans MT", 12))
submit_button.grid(row=19, column=14)

button1 = tk.Button(window, text="Exit", command=open_file1, bg="#cfc080", fg="white", padx=10, pady=5, font=("Gill Sans MT", 12))
button1.grid(row=19, column=15)

# run the tkinter event loop
window.mainloop()

