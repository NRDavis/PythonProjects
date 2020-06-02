import cv2
import numpy
import os
import platform

print("Welcome, "+platform.system()+" user.")
print("Your current working directory is: "+os.getcwd())
print("This program will allow you to read images using the OpenCV library.")
print("Enter the name of an image file within the local directory:")
image_ans = input()
print("Would you like to view this in color(1) or in grayscale(2)?")
view_ans = input()
if view_ans == 2:
    print("Displaying image in grayscale.")
    view_ans = 0
elif view_ans == 1:
    print("Displaying image in color")
else:
    print("Default display in color.")
    view_ans=1
    
img = cv2.imread(image_ans, view_ans)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()