import sys 
import cv2
import time
import numpy as np
import imutils

def find_circles(frame, mask):
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    if len(contours)>0:
        c = max(contours, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["00"]))

        if radius>10:
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0,255,255),2)
            cv2.circle(frame, center, 5, (0,0,0), -1)
    return center

