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

    def setup_ui(self):
        self.start_button = ttk.Button(
            self.root, text="Start", command=self.start_filter)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(
            self.root, text="Stop", command=self.stop_filter)
        self.stop_button.pack(pady=10)

    def start_filter(self):
        self.run_filter = True
        self.process_frames()

    def stop_filter(self):
        self.run_filter = False
        cv2.destroyAllWindows()

    def process_frames(self):
        if not self.run_filter:
            return

        ret, frame = self.cap.read()
        if ret:
            grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Live Greyscale Filter", grey_frame)
            cv2.waitKey(20)

        self.root.after(10, self.process_frames)
