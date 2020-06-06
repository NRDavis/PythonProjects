import numpy as np
import cv2

img = cv2.imread("astronaut_sunrise.jpg", cv2.IMREAD_COLOR)

# drawing a line                openCV using BGR
#cv2.line(img, (0, 0), (150, 150), (0, 255, 0), 15)     # image, start coord, stop coord, line width
#cv2.rectangle(img, (0,0), (150, 150), (0, 0, 255), 5)
#cv2.circle(img, (75, 75), 25, (255, 0, 0), 2)

# defining points for a polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True,(0, 255, 0))
        # true connects final point to first point

# writing
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tutorial!', (0, 130), font, 1, (0, 0, 255), 4, cv2.LINE_AA)



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()