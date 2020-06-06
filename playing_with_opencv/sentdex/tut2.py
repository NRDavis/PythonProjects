import numpy as np 
import cv2

cap = cv2.VideoCapture(1) 								# we call external camera for video capture
while(1):
    ret, frame = cap.read()								# we return true/false value, the capture frame		
    #print(height)
    #cv2.imshow("Cropped Image", crop_img)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)							# we display the camera's output
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break											# we have a break statement

cap.release()											# we unlink the camera feed from the program 
cv2.destroyAllWindows()									# we call a destructor for the displays