import cv2
import numpy as np
import time
import subprocess
import os

from PIL import ImageGrab
from time import sleep
from PIL import Image
import pytesseract


#Run continuously unless stopped by user
while(1):

    #Select area to capture on screen using X,Y coordinates
    img=np.array(ImageGrab.grab(bbox=(50,175,700,725)))
    img_final=img

    #Default Format is BGR convert to GRAY
    img2gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)
    
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    
    ret, new_img = cv2.threshold(image_final, 150, 255, cv2.THRESH_BINARY) #180

    cv2.imshow('Threshold', new_img)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    
    dilated = cv2.dilate(new_img, kernel, iterations=9)  # dilate , more the iteration more the dilation

    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours


    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 35 and h < 35:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

        '''
        #you can crop image and send to OCR  , false detected will return no text :)
        cropped = img_final[y :y +  h , x : x + w]

        s = file_name + '/crop_' + str(index) + '.jpg' 
        cv2.imwrite(s , cropped)
        index = index + 1

        '''
    # show original image with added contours to disk
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('overlap', img_rgb)


    #press esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
