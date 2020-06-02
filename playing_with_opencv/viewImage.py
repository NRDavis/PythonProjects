import cv2
import numpy

img = cv2.imread("wolfpack.jpg", 1)     # simple script to demonstrate how we open up an image in full color and in grayscale using opencv2
gray = cv2.imread("wolfpack.jpg", 0)

cv2.imshow("wolfpack", img)             # the output windows are display on screen
cv2.imshow("grayscale", gray)

cv2.waitKey(0)                                   # The program starts to wait. upon pressing any key, the system will terminate it's wait process and continue with the script.
cv2.destroyAllWindows()                     # the program closes all windows