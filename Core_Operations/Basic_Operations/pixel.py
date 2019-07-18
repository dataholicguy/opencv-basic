import cv2
import numpy as np

img = cv2.imread('pic1.png')

# Display image
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Remember that in OpenCV color is BGR not RGB

# Access a pixel value by its row and column coordinates
px = img[424, 757]
print(px)   # print bgr color of the pixel 'px'

# Modify the pixel values the same way
img[100, 100] = [255, 255, 255] # change color of pixel(100, 100) to white
print(img[100, 100])

# Display image
# You'll see a pixel at position (100, 100) become white (zoom to see)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Better pixel accessing and editing method
# accessing pixel value
print(img.item(100, 100, 2))    # 255

# modifying value
img.itemset((100, 100, 2), 0)
print(img.item(100, 100, 2))    # 0
