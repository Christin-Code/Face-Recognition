import subprocess
import tkinter as tk
import cv2

def run_script():
    subprocess.call(['python', 'EncodeGenerator.py'])

window = tk.Tk()

button = tk.Button(window, text="Execute Script", command=run_script)
button.pack()

window.mainloop()
