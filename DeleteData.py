import tkinter as tk
from PIL import Image, ImageTk
import pyrebase
import os
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
window.title("Delete Data to Firebase")

# load the background image and resize it
image = Image.open("AHimg.jpg")
image = image.resize((1920, 1080), Image.ANTIALIAS)

# create a PhotoImage object from the image file
photo = ImageTk.PhotoImage(image)

# create a label widget for the background image and place it behind all other widgets
background_label = tk.Label(window, image=photo, compound="center")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

name_label = tk.Label(window, text="Titan Property Management", bg="#ffffff", fg="#2b34d9", font=("Castellar", 24, "bold"))
name_label.grid(pady=20, row=0, column=15)

title_label = tk.Label(window, text="Delete Employee Data", width=20, height=3, bg="#ffffff", fg="#9040c2", font=("Gabriola", 21, "bold"))
title_label.grid(row=1, column=5)

id_label = tk.Label(window, text="ID", width=15, height=1, bg="#ffffff", font=("Gabriola", 16, "bold"))
id_entry = tk.Entry(window, font=("Bahnschrift", 16))
id_label.grid(row=2, column=15)
id_entry.grid(row=2, column=16)

# set the size of the window
window.geometry("1920x1080")

window.configure(bg="#ffb59e")

# function to insert data into Firebase
def update_data():
    data = {
        "Id": id_entry.get()
    }
    messagebox.showinfo("Success", "Data has been Deleted successfully!")
    db.child("Employees").child(id_entry.get()).remove()
    id_entry.delete(0, tk.END)
    open_file1()

# create a button to insert data into Firebase
submit_button = tk.Button(window, text="Delete", command=update_data,  bg="#37ad69", fg="white", padx=10, pady=5, font=("Gill Sans MT", 12))
submit_button.grid(row=18, column=15)

button1 = tk.Button(window, text="Exit", command=open_file1, bg="#f00f07", fg="white", padx=10, pady=5, font=("Gill Sans MT", 12))
button1.grid(row=18, column=16)

# run the tkinter event loop
window.mainloop()
