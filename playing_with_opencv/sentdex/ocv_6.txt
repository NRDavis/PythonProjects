import cv2
import numpy as np

# tutorial 6 - thresholding

img = cv2.imread('astronaut_sunrise.jpg')
retval, threshold = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 50, 255, cv2.THRESH_BINARY)

# we create an adaptive threshold to respond to the needs of our program
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)                        # This can be used to eliminate shadows, etc
                                                # imagine cleanining up a scan of a book, with shadows caused by curves


#cv2.imwrite('astroGaus.png', gaus)
#cv2.imwrite('astroThreshold_120.png', threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()