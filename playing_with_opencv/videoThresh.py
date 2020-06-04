import cv2
import numpy as np


cap = cv2.VideoCapture(0)			# displaying the default web cam

while 1:
    _, frame = cap.read()		# we read the video feed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # we convert video feed to gray
    retVal, thresh1 = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)          # we implement a threshold for 

    thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    blur = cv2.GaussianBlur(gray, (7,7), 0)     # we use a gaussian blur -- if you change the center argument to a higher or lower square prime, you can change the granulation
    thresh3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    #cv2.imshow("frame", frame)
    #cv2.imshow("gray", gray)                       # gray scale video feed 
    #cv2.imshow("thresh", thresh1)                  # binary threshold - duotone video 
    #cv2.imshow("thresh2", thresh2)             # adaptive gaussian threshold imposed 
    cv2.imshow("thresh3", thresh3)              # presents animated style of video 
    
    if cv2.waitKey(5) & 0xFF == 27:
        break
	
cv2.destroyAllWindows()
