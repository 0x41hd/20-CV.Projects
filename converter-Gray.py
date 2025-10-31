import cv2
import numpy as np
from tkinter import Tk, filedialog, Button, Label
from tkinter import N, S, E, W


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg* .jpeg* .png* .bmp* .tiff")])
    if file_path:
        convert_to_graysacale(file_path)


def convert_to_grayscale(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
