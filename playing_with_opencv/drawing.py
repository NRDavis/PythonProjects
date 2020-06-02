import cv2
import numpy as np

# we create a black image
create = np.zeros((512,512,3), np.uint8)    # we populate a multidimensional array with 8bit integer values
cv2.line(create, (12,12), (500, 500), (0,255,0), 2)
cv2.line(create, (12,500), (500, 12), (255,0,0),2)
cv2.circle(create, (255,255), 20, (0,0,255), -1)

gen = np.zeros((512,512,3), np.uint8)       # creates black rectangle 
for i in range(0,511):
    for j in range(0,511):
        gen[i][j][0] = 255                              # we use additive color to set each of the pixels to white
        gen[i][j][1] = 255 
        gen[i][j][2] = 255 


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(gen,'OpenCV',(10,500), font, 4,(255,255,0),2,cv2.LINE_AA)



raw = cv2.imread("redCar.png", 1)
img = cv2.imread("redCar.png", 1)        # we read the image file in full color
            # image, top-left, botom-right, color, thickness, etc
cv2.rectangle(img, (130,140), (350, 240), (0,0,255))    # we create a box around the car
            # image, center-point, diameter, color, 
cv2.circle(img, (260, 205), 22, (0,255,0), -1 )         # we cover the wheels with green circles
cv2.circle(img, (330, 190), 14, (0,255,0), -1 )

cv2.imshow("Created image", create)
cv2.imshow("white?", gen)
cv2.imshow("Raw Image", raw)
cv2.imshow("Hot Wheels", img)


cv2.imwrite("./generated/hotwheels.png", img)
cv2.imwrite("./generated/white.jpg", gen)
cv2.imwrite("./generated/shapes.png", create)


cv2.waitKey(0)
cv2.destroyAllWindows()			# we close all active windows