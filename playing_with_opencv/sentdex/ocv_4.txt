import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)     # input source, full color original feed

# typical image analysis workflow
    # obtain source
    # convert to grayscale and determine critical points
    # draw box around item within color feed, while obtaining points from the grayscale feed

#px = img[55, 55] # location and color values
#print(px)       # prints color value for this pixel

#img[55, 55] = [255, 255, 255]      # here, we actually modify the color of the pixel

# region of image - subimage of an image
roi = img[100:150, 100:150] = [255, 255, 255]
#print(roi)

watch_face = img[37:111, 107:194]       # region of an image
img[0:74, 0:87] = watch_face        # must be same size

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()