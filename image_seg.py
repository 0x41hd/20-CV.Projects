import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import Button, Label


def select_image():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    image = cv2.imread(filepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    segment_image(image)
