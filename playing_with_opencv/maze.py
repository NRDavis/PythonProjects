import cv2
import numpy as np



img = np.zeros((512,512,3), np.uint8)           # we allocate a 512x512x3 multidimensional array with all values set to black


def init_board():
    
    for i in range(0,511):
        for j in range (0,511):
                img[i][j][0] = 120
                img[i][j][0] = 120
                img[i][j][0] = 120
            
    border_width = 3
    border_color = (155, 255, 10)
    cv2.line(img, (10,12), (10,502), border_color, border_width)       # left
    cv2.line(img, (10,502), (502,502), border_color, border_width)        # bottom
    cv2.line(img, (502, 502),(502,10),border_color, border_width)                             # right
    cv2.line(img, (10,10),(502,10),border_color, border_width)                             # top
    
         #  Border: 10,     92, 174,    256, 338,       420, 502
    # drawing maze borders 
    cv2.line(img, (10,420),(442, 420), border_color, border_width)      # bottom most border_color
    cv2.line(img, (72, 338), (502, 338), border_color, border_width)
    cv2.line(img, (10,256),(442, 256), border_color, border_width)
    cv2.line(img, (72, 174), (502, 174), border_color, border_width)
    cv2.line(img, (10,92),(442, 92), border_color, border_width)
    
    red = (0,0,255)
    #cv2.circle(img, ())                #   10,         51, x92, 143        235, 327        419
    for i in range(0,5):
        for j in range(0,6):
                cv2.circle(img, (51+j*82,51+i*82), 5, red, -1)

# initialize square ----- moving figure
    yellow = (0, 211, 255)
    cv2.rectangle(img, (20,492), (30,482), yellow, -1)

    cv2.putText(img, "Maze", (60, 482), cv2.FONT_HERSHEY_SIMPLEX, 2, yellow, 2)
    cv2.putText(img, "play with awsd", (230, 452), cv2.FONT_HERSHEY_SIMPLEX, 1, yellow, 2)
    cv2.putText(img, "r=reset, q=quit", (230, 482), cv2.FONT_HERSHEY_SIMPLEX, 1, yellow, 2)



init_board()                                        # we create a maze image for a possible game
cv2.imshow("creation", img)
cv2.waitKey(0)
cv2.destroyAllWindows()