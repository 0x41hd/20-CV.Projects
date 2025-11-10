import cv2
import sys


def select_tracker(tracker_type):
    if tracker_type == "BOOSTING":
        return cv2.legacy.TrackerBoosting_create()
    elif tracker_type == "MIL":
        return cv2.TrackerMIL_create()
    elif tracker_type == "KCF":
        return cv2.TrackerKCF_create()
    elif tracker_type == "TLD":
        return cv2.legacy.TrackerTLD_create()
    elif tracker_type == "MEDIANFLOW":
        return cv2.legacy.TrackerMedianFlow_create()
    elif tracker_type == "MOSSE":
        return cv2.legacy.TrackerMOSSE_create()
    elif tracker_type == "CSRT":
        return cv2.TrackerCSRT_create()
    else:
        raise ValueError("Unsupported tracker type")
