import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk
from PIL import Image, ImageTk

# Initialize Firebase database credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facedetectiondatabase-7fe17-default-rtdb.firebaseio.com/"
})

# Create a Tkinter GUI
root = tk.Tk()
root.title("Update Attendance")
root.geometry("1620x780")

# Load and display an image
img = Image.open("build1.jpg")
img = img.resize((1620, 780), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0)

# Create a label and entry widget for employee ID
id_label = tk.Label(root, text="Enter Employee ID:", font=("Gabriola", 14), bg="#FFFFFF", fg="#000000")
id_label.place(relx=0.3, rely=0.5, anchor="center")
emp_id = tk.Entry(root, font=("Gabriola", 14), bg="#FFFFFF", fg="#000000", width=20)
emp_id.place(relx=0.5, rely=0.5, anchor="center")

# Create a label to display current attendance value
attendance_label = tk.Label(root, text="Attendance:", font=("Gabriola", 14), bg="#FFFFFF", fg="#000000")
attendance_label.place(relx=0.3, rely=0.6, anchor="center")
attendance_value = tk.Label(root, text="", font=("Gabriola", 14), bg="#FFFFFF", fg="#000000")
attendance_value.place(relx=0.5, rely=0.6, anchor="center")

# Function to update attendance value in Firebase
def update_attendance():
    # Get employee ID from entry widget
    id = emp_id.get()

    # Retrieve current attendance value from Firebase
    ref = db.reference('Employees/' + id + '/total_attendance')
    total_attendance = ref.get()

    # Increment attendance value by 1 and update in Firebase
    ref.set(total_attendance + 1)

    # Update attendance label in GUI to display new attendance value
    attendance_value.config(text=str(total_attendance + 1))

# Create a button to update attendance
update_button = tk.Button(root, text="Update Attendance", font=("Gabriola", 14), bg="#FFFFFF", fg="#000000", command=update_attendance)
update_button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
