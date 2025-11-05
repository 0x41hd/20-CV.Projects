import cv2
import tkinter as tk
from tkinter import ttk


class LiveGreyscaleFilter:
    def __init__(Self, root):
        self.root = root
        self.root.title("Live Greyscale Filter")
        self.run_filter = False
        self.setup_ui()
        self.cap = cv2.VideoCapture(0)
