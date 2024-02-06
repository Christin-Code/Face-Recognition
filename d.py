import tkinter as tk
from PIL import Image, ImageTk
import os

# Define company information
company_name = "About us \n \n Titan Property Management\n"
company_description = "Titan is a small company that specializes in providing various services like carpet washing, vacuuming, painting, plumbing, deep cleaning, electrical work, civil work, \n and brass polishing. The company has a team of skilled and experienced professionals who are dedicated to delivering high-quality services to their clients.\n The company prides itself on its commitment to providing excellent customer service and ensuring that their clients are satisfied with the work done.\n Titan also uses the latest tools and equipment to ensure that the work is done efficiently and effectively.\n Titan believes in transparency, and as such, they ensure that their clients are informed about the work being done and the costs involved. The company also offers \n competitive pricing for their services, making it an excellent option for those looking for quality services at affordable rates.\n Overall, Titan is a reliable and professional company that provides top-notch services to its clients."


# Create the GUI
root = tk.Tk()
root.title("Moving Images Example")
root.geometry("1920x1080")
root.configure(bg="#ffffff")

# Define the grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

# Create a Label with the company name and description
company_label = tk.Label(root, text=f"{company_name}, \n{company_description}", font=("Times New Roman",15, "bold"), justify="center", bg="#ffffff", fg="#333333", pady=20)
company_label.pack(side="top", fill="both", expand=True)
company_label.grid(row=0, column=0, sticky="nsew")

# Create a Canvas with a white background
canvas = tk.Canvas(root, bg="#ffffff", highlightthickness=0)
canvas.grid(row=3, column=0, sticky="nsew")

# Define a list of image filenames
image_filenames = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Create an empty list to hold the PhotoImage objects
photo_images = []

# Set the desired size of the images
desired_size = (200, 200)

# Load and resize the first image
current_image_index = 0
image = Image.open(image_filenames[current_image_index])
image = image.resize(desired_size)
photo = ImageTk.PhotoImage(image)
photo_images.append(photo)

# Create the first image on the Canvas
canvas_image = canvas.create_image(0, 0, anchor="nw", image=photo_images[current_image_index])

# Define a function to move the images
def move_images():
    global current_image_index, canvas_image

    # Move the current image to the right by 5 pixels
    canvas.move(canvas_image, 7, 0)

    # Check if the current image has gone off the canvas
    bbox = canvas.bbox(canvas_image)
    if bbox[2] > canvas.winfo_width():
        # Move the current image to the left side of the canvas
        canvas.coords(canvas_image, -bbox[2], bbox[1])

        # Load and resize the next image and create it on the canvas
        current_image_index = (current_image_index + 1) % len(image_filenames)
        image = Image.open(image_filenames[current_image_index])
        image = image.resize(desired_size)
        photo = ImageTk.PhotoImage(image)
        photo_images.append(photo)
        canvas_image = canvas.create_image(0, bbox[1], anchor="nw", image=photo_images[current_image_index])


    # Call this function again after 50 milliseconds
    root.after(50, move_images)


# Call the move_images function to start moving the images
move_images()

def open_file1():
    os.system('python Home.py')

# button1 = tk.Button(root, text="Home", command=open_file1, bg="#3498db", fg="white", padx=10, pady=5, font=("Helvetica", 14))
# button1.pack(side="right", padx=10, pady=10)

reg_button = tk.Button(text='Home', command=open_file1, bg="#48B9C7", fg="white", padx=10, pady=5, bd=3, font=("Helvetica", 10))
reg_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
# Run the GUI
root.mainloop()