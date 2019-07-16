import cv2
import numpy as np

# Load a background image
img = cv2.imread('bears.png', 1)

# Put texts
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Bare Bears', (430, 410), font, 4, (0, 0, 0), 5, cv2.LINE_AA)

# Save image
cv2.imwrite('logo.png', img)

# Display
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
