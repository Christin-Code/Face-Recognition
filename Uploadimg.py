import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os
import subprocess


def open_file1():
    os.system('python AdminHome.py')

#
# def run_script():
#     subprocess.call(['python', 'EncodeGenerator.py'])


# Initialize Firebase app and storage client
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'facedetectiondatabase-7fe17.appspot.com'
})
bucket = storage.bucket()

# Create the main window
window = tk.Tk()
window.title("Upload Image to Firebase Storage Bucket")

# Set the window size
window.geometry("1920x1080")

# load the background image and resize it
image = Image.open("12.jpg")
image = image.resize((1920, 1080), Image.ANTIALIAS)

# create a PhotoImage object from the image file
photo = ImageTk.PhotoImage(image)

# create a label widget for the background image and place it behind all other widgets
background_label = tk.Label(window, image=photo, compound="center")
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create a function to open the file system and get the image path
def select_image():
    # Open a file dialog and get the image path
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image",
                                           filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        # Upload the image to the Firebase Storage Bucket
        try:
            # Upload the image to the Firebase Storage Bucket
            blob = bucket.blob("Images/" + file_path.split("/")[-1])
            blob.upload_from_filename(file_path)
            messagebox.showinfo("Success", "Image uploaded to Firebase Storage Bucket!")
        except:
            messagebox.showerror("Error", "Failed to upload image to Firebase Storage Bucket.")

        # Create a PIL Image object from the selected image file
        image = Image.open(file_path)

        # Resize the image to fit the window size
        image = image.resize((216, 216), Image.ANTIALIAS)

        # Create a Tkinter PhotoImage object from the PIL Image object
        photo_image = ImageTk.PhotoImage(image)

        # Add the image to the project's Images folder
        image_name = os.path.basename(file_path)
        save_path = os.path.join(os.getcwd(), "Images", image_name)
        image.save(save_path)

        # Create a label to display the image
        image_label = tk.Label(window, image=photo_image)
        image_label.pack()


# Create a button to select an image
button = tk.Button(window, text="Select Image", command=select_image, bg="#ebc444", fg="#1a264f",font=("Gill Sans MT", 12, "bold"))
button.pack()

button1 = tk.Button(window, text="Exit", command=open_file1, bg="#f00f07", fg="white", padx=10, pady=5, font=("Gill Sans MT", 12))
button1.pack()


# Start the Tkinter event loop
window.mainloop()
