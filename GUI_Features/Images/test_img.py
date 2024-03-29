import numpy as np
import cv2

img = cv2.imread('pic1.png', 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:     # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('barebears.png', img)
    cv2.destroyAllWindows()
