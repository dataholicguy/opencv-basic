import numpy as np
import cv2

# Create an image
img = np.zeros((512, 512, 3), np.uint8)

# Draw ellipse
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)

# Display image
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
