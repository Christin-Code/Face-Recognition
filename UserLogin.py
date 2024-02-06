import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('serviceAccountKey.json')  # Path to your Firebase Admin SDK JSON file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://facedetectiondatabase-7fe17-default-rtdb.firebaseio.com/'  # Your Firebase Realtime Database URL
})
root = tk.Tk()
root.title('Login')
root.geometry("1920x1080")

# load the background image and resize it
image = Image.open("logback2.jpg")
image = image.resize((1920, 1080), Image.ANTIALIAS)  # Resampling method recommended by Pillow

# create a PhotoImage object from the image file
photo = ImageTk.PhotoImage(image)

# create a label widget for the background image and place it behind all other widgets
background_label = tk.Label(root, image=photo, compound="center")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create a frame for the login widgets
login_frame = tk.Frame(root, bg="#f5faf8", bd=3, relief=tk.RIDGE)
login_frame.pack(padx=90, pady=140)

# add the logo image
logo_image = Image.open("loglogo.png")
logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(login_frame, image=logo_photo, bg="#f5faf8")
logo_label.pack(pady=20)

# create a label widget for the title Times New Roman
title_label = tk.Label(login_frame, text='Login', font=('Times New Roman', 35), fg='#f7208c', bg="#f5faf8")
title_label.pack(pady=20)

# create the widgets for the login form
tk.Label(login_frame, text='Username: ', fg='#6826ed', bg="#f5faf8", font=("Rage Italic", 14)).pack(padx=10, pady=10)
login_username_entry = tk.Entry(login_frame, width=40)
login_username_entry.pack(padx=10, pady=10)

tk.Label(login_frame, text='Password: ', fg='#6826ed', bg="#f5faf8", font=("Rage Italic", 14)).pack(padx=10, pady=10)
login_password_entry = tk.Entry(login_frame, show='*',  width=40)
login_password_entry.pack(padx=10, pady=10)

# create the login and register buttons
login_button = tk.Button(login_frame, text='Login', command=lambda: login(), bg="#f7208c", fg="white", padx=10, pady=5, bd=3, font=("Times New Roman", 10))
login_button.pack(side=tk.LEFT, padx=10, pady=20)

reg_button = tk.Button(login_frame, text='Register', command=lambda: open_file2(), bg="#f7208c", fg="white", padx=10, pady=5, bd=3, font=("Times New Roman", 10))
reg_button.pack(side=tk.RIGHT, padx=10, pady=20)

root.geometry("1920x1080")

def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    # Check if the user exists in the database
    users_ref = db.reference('Login')
    user_ref = users_ref.child(username)
    if user_ref.get() is None:
        tk.messagebox.showerror('Error', 'Invalid username or password')
        return

    # Check if the password is correct
    if user_ref.child('password').get() != password:
        tk.messagebox.showerror('Error', 'Invalid username or password')
        return

    tk.messagebox.showinfo('Success', 'Login successful')
    login_username_entry.delete(0, tk.END)
    login_password_entry.delete(0, tk.END)
    open_file1()


def open_file1():
    os.system('python EmployeeHome.py')

def open_file2():
    os.system('python UserRegister.py')


root.mainloop()
