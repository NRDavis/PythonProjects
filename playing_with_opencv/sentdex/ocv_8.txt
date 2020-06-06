import cv2
import numpy as np

# tutorial 8 - removing noise                       -- paused at 4.02
# simple steps - blurring and smoothing

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()       # underscore denotes it's not saved to anything - its useless
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150, 0, 0])    # hue, saturiation, value
    upper_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)   # where there are ones in our mask, we show the frame
    res = cv2.bitwise_and(frame, frame, mask=mask)  # within our frame, we find items that are present within both the frame and the mask... ie we select pixels of the same color
    #dark_red = np.unit8([[12,22,121]])
    #dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)


    # we're going to use averaging
    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(res, -1, kernel)            # smooths everything out, but loses clarity
    blur = cv2.GaussianBlur(res, (15, 15), 0)

    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)        # filtering
    cv2.imshow('blur', blur)                # used for a series of filters

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()