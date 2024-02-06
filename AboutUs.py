import tkinter as tk
from PIL import ImageTk, Image
import os

# Define company information
company_name = "Titan Property Management"
company_description = "Titan is a small company that specializes in providing various services like carpet washing, vacuuming, painting, plumbing, deep cleaning, electrical work, civil work, \n and brass polishing. The company has a team of skilled and experienced professionals who are dedicated to delivering high-quality services to their clients.\nThe company prides itself on its commitment to providing excellent customer service and  ensuring that their clients are satisfied with the work done.\n Titan also uses the latest tools and equipment to ensure that the work is done efficiently and effectively.Titan believes in transparency,\n and as such, they ensure that their clients are informed about the work being done and the costs involved. The company also offers competitive pricing for \n their services, making it an excellent option for those looking for quality services at affordable rates.\nOverall, Titan is a reliable and professional company that provides top-notch services to its clients."
# Define GUI window
window = tk.Tk()
window.title("About Us")
window.geometry("1920x1080")
window.configure(bg="#ffffff")

# Define GUI widgets
title_label = tk.Label(window, text=company_name, font=("Times New Roman", 20, "bold"), bg="#ffffff", fg="#000000")
description_label = tk.Label(window, text=company_description, font=("Century", 12), bg="#ffffff", fg="#000000")

# Layout GUI widgets
title_label.pack(pady=10)
description_label.place(x=20, y=200, width=1500)
# description_label.pack(padx=10, pady=10)

def open_file1():
    os.system('python Home.py')

button1 = tk.Button(window, text="Home", command=open_file1, bg="#3498db", fg="white", padx=10, pady=5, font=("Helvetica", 14))
button1.pack(side="right", padx=10, pady=10)
# Run GUI loop
window.mainloop()
