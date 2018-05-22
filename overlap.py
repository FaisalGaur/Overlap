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

    # create an image filled with zeros, single-channel, same size as img.
    blank = np.zeros( img.shape[0:2] )

    count = -1

    img1 = blank.copy()
    img2 = blank.copy()

    cv2.drawContours(img1, contours, 0, 1, thickness=-1)
    cv2.drawContours(img2, contours, 1, 1, thickness=-1)
    
    overlap = cv2.bitwise_or(img1, img2)
    
    cv2.imshow('contour', overlap)

    d={}

    '''
    for contour in contours:

        count = count+1
        cnt = contours[count]
        #cv2.drawContours(img, [cnt], 0, 1, thickness=-1)
        #d["pic{0}".format(count)] = cv2.drawContours(img, contours, count, (0,255,0), thickness=-1)
        #filename = "pic{0}".format(count)
        filename = cv2.drawContours(blank.copy(), contours, 3, 1, thickness=-1)
        #cv2.imshow('contour', filename)
        #print filename
        #cv2.imshow('contour', filename)
        '''
        
  
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    cv2.imshow('overlap', img_rgb)



    #press esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
