import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a green rectangle at the top-right corner of image
cv2.rectangle(img, (256, 0), (510, 256), (0, 255, 0), 3)

# Display image
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
