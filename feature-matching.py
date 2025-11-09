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


def feature_matching():
    if img1 is None or img2 is None:
        return

    orb = cv2.ORB_create()

    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)

    matches = sorted(matches, key=lambda x: x.distance)

    img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2,
                                  matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2.imshow('Feature Matching', img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
