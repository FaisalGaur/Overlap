"""
Install following through pip install <module>
opencv-python
pillow
"""

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


def main():
    x_start, y_start, width, height = select_region_of_interest()
    # Run continuously unless stopped by user
    while True:
        # capture at 30 frames per second 1/30
        time.sleep(0.033)

        # Select area to capture on screen using X,Y coordinates
        bgr_img = np.array(ImageGrab.grab(bbox=(x_start, y_start, width, height)))

        # convert BGR to RGB color space
        rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

        # display the image in a window
        cv2.imshow('Selected ROI', rgb_img)

        # Insert code to perform your image processing

        # press ESC stop
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    # close all image windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


