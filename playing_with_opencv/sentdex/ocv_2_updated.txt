import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))       # we save video


if not cap.isOpened():
    print("Video stream is not available")          # if stream not available, print statement
    exit()

while cap.isOpened():
    ret, frame = cap.read()                         # allocate frame object from feed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert video feed to gray scale
    out.write(frame)
    cv2.imshow('Analysis', gray)                  # display video feed
    cv2.imshow('Natural', frame)

    if not ret:
        print("can't receive frame - Exiting")      # print if bad
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()