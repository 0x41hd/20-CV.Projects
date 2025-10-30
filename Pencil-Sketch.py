import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Dictionary for store PIL image
images = {"original": None, "sketch": None}


def open_file():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    img = cv2.imread(filepath)
    display_image(img, original=True)
    sketch_image = convert_to_sketch(img)
    display_image(sketch_img, original=False)


