import tkinter as tk
import os
from tkinter import *
from PIL import Image, ImageTk

def open_file1():
    os.system('python AdminLogin.py')

def open_file2():
    os.system('python UserLogin.py')

def open_file3():
    os.system('python main.py')

def open_file4():
    os.system('python d.py')


root = tk.Tk()
root.title("Titan Property Management")
root.geometry("1920x1080")
root.configure(bg="#fcfcfc")

# Add a company logo
logo_path = "company_logo.jpg"
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_resized = logo_img.resize((150,150), Image.ANTIALIAS)
    logo_tk = ImageTk.PhotoImage(logo_resized)
    logo_label = tk.Label(root, image=logo_tk, bg="#F9F9F9")
    logo_label.image = logo_tk
    logo_label.pack(pady=20)

# Add a company name
name_label = tk.Label(root, text="Titan Property Management", font=("Times New Roman", 40, "bold"), fg="#2b34d9", bg="#F9F9F9")
name_label.pack(pady=10)

# Add a company slogan
slogan_label = tk.Label(root, text="Experience the excellence of Titan's services for a brighter tomorrow.", font=("Freestyle Script", 18, "bold"), fg="#58a862", bg="#F9F9F9")
slogan_label.pack(pady=10)

# Add a navigation menu
menu_frame = tk.Frame(root, bg="#3C3C3C")
menu_frame.pack(side="top", fill="x")

menu_items = [
    {"text": "Admin Login", "command": open_file1,  "bg": "#48B9C7"},
    {"text": "Employee Login", "command": open_file2, "bg": "#48B9C7"},
    {"text": "Face Recognition Attendance System", "command": open_file3, "bg": "#48B9C7"},
    {"text": "About Us", "command": open_file4, "bg": "#48B9C7"},
]

for item in menu_items:
    button = tk.Button(menu_frame, text=item["text"], command=item["command"], bg=item["bg"], fg="white", padx=10, pady=5, bd=0, font=("Helvetica", 14, "bold"), activebackground="#3C3C3C", activeforeground="white")
    button.pack(side="left", padx=15, pady=10, anchor="center")

# Add images below the menu_frame in a horizontal way
image_frame = tk.Frame(root, bg="#F9F9F9")
image_frame.pack(pady=20)

image_paths = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpeg", "image5.jpg", "image6.jpg" ] # replace this with the paths to your images
for path in image_paths:
    if os.path.exists(path):
        img = Image.open(path)
        img_resized = img.resize((200, 250), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img_resized)
        img_label = tk.Label(image_frame, image=img_tk, bg="#F9F9F9")
        img_label.image = img_tk
        img_label.pack(side="left", padx=20)

# Add a footer
footer_label = tk.Label(root, text="Titan property  management services\n #125/30 ,16th cross,3rd stage ,\nprakruti layout hennur,kalyan nagar post \nbanglore 560043", font=("Helvetica", 8), fg="#3C3C3C", bg="#F9F9F9")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
