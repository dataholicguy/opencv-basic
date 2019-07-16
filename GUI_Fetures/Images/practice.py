import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread('japan.jpg', 0)

exit = False
while not exit:
    print('Mode:')
    print('1. OpenCV')
    print('2. Matplotlib')
    print('3. Exit')

    # Display image
    choice = int(input('>>> Your choice: '))
    print()
    if choice == 1:
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 2:
        plt.imshow(img, cmap='gray', interpolation='bicubic')
        plt.xticks([]), plt.yticks([])
        plt.show()
    elif choice == 3:
        exit = True
