import cv2
import numpy as np

img = cv2.imread('messi1.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Splitting B, G, R channels
b, g, r = cv2.split(img)
print('B: ', b)
print('G: ', g)
print('R: ', r)

img1 = cv2.merge((b, g, r))
cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.imshow('image1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
