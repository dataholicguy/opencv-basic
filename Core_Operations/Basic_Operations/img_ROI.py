import cv2
import numpy as np

# load image
img = cv2.imread('messi1.jpg')

# display image to find ball index
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# select the ball
ball = img[280:340, 330:390]

# copy the ball to another region
img[273:333, 100:160] = ball

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
