import cv2
import numpy as np
from tkinter import Tk, filedialog, Button, Label
from tkinter import N, S, E, W


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg* .jpeg* .png* .bmp* .tiff")])
    if file_path:
        convert_to_grayscale(file_path)
