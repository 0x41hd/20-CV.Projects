import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def open_files():
    files = filedialog.askopenfilenames(title='Select Images')
    if len(files) < 2:
        messagebox.showerror("Error", "Please select at least two images.")
        return
    for file in files:
        image_paths.append(file)
    messagebox.showinfo("Success", "Selected {} images.".format(len(files)))
