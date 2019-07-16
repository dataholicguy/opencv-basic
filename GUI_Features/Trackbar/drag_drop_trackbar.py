import cv2
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1

def nothing(x):
    pass

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('paint')

# Create trackbars for change color
cv2.createTrackbar('B', 'paint', 0, 255, nothing)
cv2.createTrackbar('G', 'paint', 0, 255, nothing)
cv2.createTrackbar('R', 'paint', 0, 255, nothing)
cv2.createTrackbar('Brush Size', 'paint', 0, 20, nothing)

# Get current position of four trackers
def get_position():
    global r, g, b, s
    b = cv2.getTrackbarPos('B', 'paint')
    g = cv2.getTrackbarPos('G', 'paint')
    r = cv2.getTrackbarPos('R', 'paint')
    s = cv2.getTrackbarPos('Brush Size', 'paint')
    return (b, g, r, s)

# Draw with mouse event
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
            else:
                cv2.circle(img, (x, y), s, (b, g, r), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
        else:
            cv2.circle(img, (x, y), s, (b, g, r), -1)

while (1):
    cv2.imshow('paint', img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('m'):
        mode = not mode
    else:
        get_position()
        cv2.setMouseCallback('paint', draw)
