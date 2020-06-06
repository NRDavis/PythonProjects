import cv2
# Nathan Davis, copying and pasting items from

cap = cv2.imread('astronaut_sunrise.jpg', cv2.IMREAD_COLOR)             # Color display of feed

black = cv2.imread('black.jpg', cv2.IMREAD_COLOR)                       # black image for source -

gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

roi_gray = gray[270:550, 250:500]                                       # crop of grayscale
roi_color = cap[270:550, 250:500]   # 280, 250

black[0:280, 0:250, 0] = roi_gray
black[0:280, 0:250, 1] = roi_gray
black[0:280, 0:250, 2] = roi_gray       # each individual color spectrum bgr must be draw onto item

black[0:280, 251:501, 0] = roi_gray       # b shift
black[0:280, 502:752, 1] = roi_gray       # g shift
black[0:280, 753:1003, 2] = roi_gray      # r shift

black[0:280, 1004:1254] = roi_color       # full color
# second row
black[281:561, 0:250] = roi_color

black[281:561, 251:501, 2] = roi_gray
black[281:561, 502:752, 1] = roi_gray
black[281:561, 753:1003, 0] = roi_gray

black[281:561, 1004:1254, 0] = roi_gray
black[281:561, 1004:1254, 1] = roi_gray
black[281:561, 1004:1254, 2] = roi_gray


cv2.imwrite('astronauts.jpg', black)

cv2.imshow('pasted', black)
cv2.imshow('color', roi_color)
cv2.imshow('gray', roi_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()