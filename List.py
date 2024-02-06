import pyrebase
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import os

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

# create tkinter window
window = tk.Tk()
window.title("Employee Information")
window.geometry("1920x1080")

# load the background image and resize it
image = Image.open("12.jpg")
image = image.resize((1920, 1080), Image.ANTIALIAS)

# create a PhotoImage object from the image file
photo = ImageTk.PhotoImage(image)

# create a label widget for the background image and place it behind all other widgets
background_label = tk.Label(window, image=photo, compound="center")
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# retrieve all employee data
employees = db.child("Employees").get()

# create text widget to display employee information
employee_info = tk.Text(window, height=40, width=90)
employee_info.pack()

def show_employee_info():
    # clear the text widget
    employee_info.delete("1.0", tk.END)

    # retrieve all employee data from Firebase
    employees = db.child("Employees").get()

    # iterate over employee data and append it to the text widget
    for employee in employees.each():
        data = employee.val()
        info = f"ID: {data['Id']}\nDepartment: {data['department']}\nJoined Year: {data['joined_year']}\nLast Attendance Time: {data['last_attendance_time']}\nName: {data['name']}\nStanding: {data['standing']}\nTotal Attendance: {data['total_attendance']}\n\n"
        employee_info.insert(tk.END, info)

# # print each employee's data to the console
# for employee in employees.each():
#     print(employee.key(), employee.val())
# create button to retrieve employee information
button = tk.Button(window, text="Show Employee Details", command=show_employee_info, bg="#ebc444", fg="#1a264f", padx=10, pady=5, font=("Gill Sans MT", 12, "bold"))
button.pack()

button1 = tk.Button(window, text="Exit", command=open_file1, bg="#f00f07", fg="white", padx=10, pady=5, font=("Gill Sans MT", 12))
button1.pack()

# start the tkinter event loop
window.mainloop()