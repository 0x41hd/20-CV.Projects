import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import Scale, HORIZONTAL, Button

# Initialize the application
root = tk.Tk()
root.title("Morphological Transformations")

# Load an image from a file dialog


def load_image():
    global img, img_display
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    if img is not None:
        apply_transformations()

# Apply morphological transformations


def apply_transformations(*args):
    global img, img_display

    if img is None:  # Ensure an image is loaded before applying transformations
        return

    kernel_size = kernel_scale.get()
    operation = var.get()

    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    if operation == "Erosion":
        transformed_img = cv2.erode(img, kernel, iterations=1)
    elif operation == "Dilation":
        transformed_img = cv2.dilate(img, kernel, iterations=1)
    elif operation == "Opening":
        transformed_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    elif operation == "Closing":
        transformed_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    elif operation == "Gradient":
        transformed_img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    elif operation == "Top Hat":
        transformed_img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    elif operation == "Black Hat":
        transformed_img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

    img_display = transformed_img
    cv2.imshow('Image', img_display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
