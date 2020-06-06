# Nathan Davis - OpenCV first use
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("astronaut_sunrise.jpg", cv2.IMREAD_GRAYSCALE)        # "Marvin.jpg"

# IMREAD_GRAYSCALE  = 0
# IMREAD_COLOR      = 1
# IMREAD_UNCHANGED  = -1

cv2.imshow("image", img)        # displays image
cv2.waitKey(0)                  # waits for key to be pressed
cv2.destroyAllWindows()         # closes all windows when keys are pressed

cv2.imwrite('grayNaut.png', img)    # we save a new version of the astronaut pic as a png



# OpenCV does bgr, matplotlib does rgb
# plt.imshow(img, cmap="gray", interpolation='bicubic')       # use matplotlib to display image, alternative to cv2
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)            # plot line directly on plot
# plt.show()                                                  # display command
