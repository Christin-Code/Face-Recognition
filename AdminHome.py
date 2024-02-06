import tkinter as tk
import os
from PIL import Image, ImageTk

def open_file1():
    os.system('python AddData.py')

def open_file2():
    os.system('python UpdateData.py')

def open_file3():
    os.system('python DeleteData.py')

def open_file4():
    os.system('python RetrieveData.py')

def open_file5():
    os.system('python List.py')

def open_file6():
    os.system('python Uploadimg.py')

def open_file7():
    os.system('python Home.py')

def open_file8():
    os.system('python EncodeGenerator.py')

root = tk.Tk()
root.title("Button Example")

# Set the size and position of the window
root.geometry("1620x900")

# Set the background color of the window
root.configure(bg="#F0F0F0")

# Create a header frame
header_frame = tk.Frame(root, bg="#3305ff", height=250)
header_frame.pack(side="top", fill="x")

# Add a company name
name_label = tk.Label(header_frame, text="Titan Property Management", font=("Times New Roman", 40, "bold"), bg="#3305ff", fg="white")
name_label.pack(pady=20)

# Add a company slogan
slogan_label = tk.Label(header_frame, text="Experience the excellence of Titan's services for a brighter tomorrow.", font=("Freestyle Script", 16), bg="#3305ff", fg="white")
slogan_label.pack(pady=10)

# Create a main frame
main_frame = tk.Frame(root, bg="#ffffff")
main_frame.pack(expand=True, fill="both")

# Create a menu frame
menu_frame = tk.Frame(main_frame, bg="#3C3C3C", height=50)
menu_frame.pack(side="top", fill="x")

# Create a content frame
content_frame = tk.Frame(main_frame, bg="white")
content_frame.pack(expand=True, fill="both")

# Create buttons
button1 = tk.Button(menu_frame, text="Add New Employee", command=open_file1, bg="#aaf3fa", fg="black", padx=10, pady=5, bd=3, font=("Helvetica", 14))
button1.pack(side="left", padx=15, pady=15)

button2 = tk.Button(menu_frame, text="Update Data", command=open_file2, bg="#aaf3fa", fg="black", padx=10, pady=5, font=("Helvetica", 14))
button2.pack(side="left", padx=10, pady=10)

button3 = tk.Button(menu_frame, text="Delete Data", command=open_file3, bg="#aaf3fa", fg="black", padx=10, pady=5, font=("Helvetica", 14))
button3.pack(side="left", padx=10, pady=10)

button4 = tk.Button(menu_frame, text="Retrieve Data", command=open_file4, bg="#aaf3fa", fg="black", padx=10, pady=5, font=("Helvetica", 14))
button4.pack(side="left", padx=10, pady=10)

button5 = tk.Button(menu_frame, text="List", command=open_file5, bg="#aaf3fa", fg="black", padx=10, pady=5, font=("Helvetica", 14))
button5.pack(side="left", padx=10, pady=10)

button6 = tk.Button(menu_frame, text="Upload Image", command=open_file6, bg="#aaf3fa", fg="black", padx=10, pady=5, font=("Helvetica", 14))
button6.pack(side="left", padx=10, pady=10)

button7 = tk.Button(root, text="Home", command=open_file7, bg="#aaf3fa", fg="black", padx=10, pady=5, font=("Helvetica", 14))
button7.pack(side="left", padx=10, pady=10)

button8 = tk.Button(menu_frame, text="EncodeFile", command=open_file8, bg="#aaf3fa", fg="black", padx=10, pady=5, font=("Helvetica", 14))
button8.pack(side="left", padx=10, pady=10)

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
