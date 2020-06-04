import cv2
import numpy as np

cap = cv2.VideoCapture(0)			# we use the default web camera 

while 1:
    _, frame = cap.read()				# depending upon what our while loop returns, we read the camera feed
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)     # we convert the capture's color array from standard BlueGreenRed to HueSaturationValue
    low_green = np.array([65, 10, 10])
    upper_green = np.array([95, 255, 255])

    mask = cv2.inRange(hsv, low_green, upper_green)                 # we create a bitmap featuring, separating each of the items into 

    res = cv2.bitwise_and(frame, frame, mask = mask)            # we perform an and operation on each of the pixels, setting them high and low

    cv2.imshow("frame", frame)      # we ouput each of the video streams onto the monitor
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break                               # when we press the esc button, we exit the while loop
    
cv2.destroyAllWindows()
