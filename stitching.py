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


def stitch_images():
    paths = image_paths
    if len(paths) < 2:
        messagebox.showerror("Error", "Please select at least two images.")
        return

    images = []
    for path in paths:
        img = cv2.imread(path)
        if img is None:
            messagebox.showerror(
                "Error", "Could not read image {}".format(path))
            return
        images.append(img)

    stitcher = cv2.Stitcher_create()
    status, pano = stitcher.stitch(images)

    if status != cv2.Stitcher_OK:
        messagebox.showerror("Error", "Image stitching failed.")
        return

    display_image(pano)
    messagebox.showinfo("Success", "Images stitched successfully.")
