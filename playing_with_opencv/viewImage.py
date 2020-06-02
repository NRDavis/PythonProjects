import cv2
import numpy

img = cv2.imread("wolfpack.jpg", 1)

cv2.imshow("wolfpack", img)
cv2.waitKey(0)
cv2.destroyAllWindows()