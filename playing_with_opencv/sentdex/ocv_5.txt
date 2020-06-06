import cv2
import numpy as np			# adding a threshold
# Tutorial 5 by sentdex - adding components of multiple images into the same output file

img1 = cv2.imread("astronaut_sunrise.jpg")
img2 = cv2.imread("pythonlogo.jpg")

r, c, ch = img1.shape
print("Rows: "+str(r)+"\t\tCols: "+str(c)+"\n")

rows, cols, channels = img2.shape           # we obtain the rows, columns and channels associated with img2
roi = img1[0:rows, 0:cols]

print("Rows: "+str(rows)+"\t\tCols: "+str(cols)+"\n")

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)       # creates gray scale version of marvin
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY_INV)     # we set the minimum and maximum pass numbers
                # below 220 - converted to black
                # above 220 - converted to white
                # inverse above - hence

#cv2.imwrite("starwars_mask.png", mask) # we save the cool black-white starwars image
cv2.imshow('mask', mask)

#mask_inv = cv2.bitwise_not(mask)
#img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#img2_fv = cv2.bitwise_and(img2, img2, mask=mask)

#dst = cv2.add(img1_bg, img2_fv)
#img1[0:rows, 0:cols] = dst
#cv2.imshow('res', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()