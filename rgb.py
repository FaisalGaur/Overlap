import cv2
import numpy as np
import time
from PIL import ImageGrab

def select_region_of_interest():
    """
    Select a ROI (Region of interest) and then press ENTER or SPACE button.
    Cancel the selection process by pressing c button.
    :return: Coordinates of selected rectangle ROI on screen
    """
    image = np.array(ImageGrab.grab(bbox=None))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    r = cv2.selectROI(windowName='grab roi', img=image, showCrosshair=True, fromCenter=False)
    cv2.destroyAllWindows()
    return r[0], r[1], r[0] + r[2], r[1] + r[3]


def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
        colors = frame[y,x]
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)


x_start, y_start, width, height = select_region_of_interest()

cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)


while True:

    time.sleep(0.033)

    # Select area to capture on screen using X,Y coordinates
    bgr_img = np.array(ImageGrab.grab(bbox=(x_start, y_start, width, height)))

    # convert BGR to RGB color space
    frame = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

    cv2.imshow('mouseRGB', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

