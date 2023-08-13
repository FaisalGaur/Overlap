import cv2
import numpy as np
import time
from PIL import ImageGrab

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract-OCR\tesseract.exe'

while True:
    time.sleep(1.0)
    # Select area to capture on screen using X,Y coordinates
    # speed_limit = np.array(ImageGrab.grab(bbox=(806, 1040, 853, 1064)))
    current_speed = np.array(ImageGrab.grab(bbox=(794, 997, 868, 1069)))

    # convert BGR to RGB color space
    # speed_limit = cv2.cvtColor(speed_limit, cv2.COLOR_BGR2RGB)
    speed = cv2.cvtColor(current_speed, cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_string(speed_limit))
    print(pytesseract.image_to_string(speed))

# print(pytesseract.image_to_string('speeding.png'))
