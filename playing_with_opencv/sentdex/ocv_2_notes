import cv2
import numpy as np
										# work around for video feed, tutorial 2 - sentdex
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Video stream is not available")          # if stream not available, print statement
    exit()

while cap.isOpened():
    ret, frame = cap.read()                         # allocate frame object from feed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert video feed to gray scale
    cv2.imshow('gray frame', gray)                  # display video feed

    if not ret:
        print("can't receive frame - Exiting")      # print if bad
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()