import cv2

cap = cv2.VideoCapture(0)             # we obtain our source from the first index webcam

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not ret:
        print("Can't receive frame. Exiting...")
        break

    cv2.imshow('gray scale', gray)
    cv2.imshow('natural', frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()