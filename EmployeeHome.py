import tkinter as tk
import os
from PIL import Image, ImageTk

def open_file1():
    os.system('python MarkAttendance.py')

def open_file2():
    os.system('python Home.py')


root = tk.Tk()
root.title("Button Example")

root.geometry("1920x1080")

# Set the background color of the window
root.configure(bg="#F0F0F0")

# Create a header frame
header_frame = tk.Frame(root, bg="#3305ff", height=250)
header_frame.pack(side="top", fill="x")

# Add a company name
name_label = tk.Label(header_frame, text="Titan Property Management", font=("Times New Roman", 28, "bold"), bg="#3305ff", fg="white")
name_label.pack(pady=20)

# Add a company slogan
slogan_label = tk.Label(header_frame, text="Experience the excellence of Titan's services for a brighter tomorrow.", font=("Freestyle Script", 16), bg="#3305ff", fg="white")
slogan_label.pack(pady=10)

# Create a main frame
main_frame = tk.Frame(root, bg="#3C3C3C")
main_frame.pack(expand=True, fill="both")

# Create a menu frame
menu_frame = tk.Frame(main_frame, bg="#3C3C3C", height=50)
menu_frame.pack(side="top", fill="x")

# Create a content frame
content_frame = tk.Frame(main_frame, bg="white")
content_frame.pack(expand=True, fill="both")

# Create buttons
button1 = tk.Button(menu_frame, text="Mark Attendance", command=open_file1, bg="#aaf3fa", fg="black", padx=10, pady=5, bd=3, font=("Helvetica", 14))
button1.pack(side="left", padx=15, pady=15)

button2 = tk.Button(menu_frame, text="Home", command=open_file2, bg="#aaf3fa", fg="black", padx=10, pady=5, font=("Helvetica", 14))
button2.pack(side="left", padx=10, pady=10)

# Add images below the menu_frame in a horizontal way
image_frame = tk.Frame(root, bg="white")
image_frame.pack(pady=200)

image_paths = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpeg", "image5.jpg", "image6.jpg" ]
for path in image_paths:
    if os.path.exists(path):
        img = Image.open(path)
        img_resized = img.resize((200, 250), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img_resized)
        img_label = tk.Label(image_frame, image=img_tk, bg="#F9F9F9")
        img_label.image = img_tk
        img_label.pack(side="left", padx=20)

# Add a footer
footer_label = tk.Label(root, text="Copyright © 2023 Our Company")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
