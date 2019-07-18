import cv2
import numpy as np

img = cv2.imread('messi.jpg')

px = img[100, 300]
print(px)
blue = img[100, 300, 0]
print(blue)
green = img[100, 300, 1]
print(green)
red = img[100, 300, 2]
print(red)

px1 = img[100, 500]
print(px1)
blue1 = img.item(100, 500, 0)
print(blue1)
green1 = img.item(100, 500, 1)
print(green1)
red1 = img.item(100, 500, 2)
print(red1)

img.itemset((100, 500, 2), 255)
print(img.item(100, 500, 2))

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('image shape: ', img.shape)
print('image size: ', img.size)
print('image data type: ', img.dtype)
