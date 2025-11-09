import cv2
import numpy as np
from tkinter import Tk, filedialog, Button, Label


def select_image():
    global img1, file_path1
    file_path1 = filedialog.askopenfilename()
    if file_path1:
        img1 = cv2.imread(file_path1, cv2.IMREAD_GRAYSCALE)
        label_img1.config(text="Image 1: {}".format(file_path1.split('/')[-1]))


def select_image_2():
    global img2, file_path2
    file_path2 = filedialog.askopenfilename()
    if file_path2:
        img2 = cv2.imread(file_path2, cv2.IMREAD_GRAYSCALE)
        label_img2.config(text="Image 2: {}".format(file_path2.split('/')[-1]))
