import cv2
import numpy as np

img = cv2.imread("redCar.png", 1)        # we read the image file in full color

cv2.rectangle(img, (130,140), (350, 240), (0,0,255))

cv2.imshow("car", img)
cv2.waitKey(0)
cv2.destroyAllWindows()			# we close all active windows