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

    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # get contours

    myList = []

    for contour in contours:
        # get rectangle bounding contour

        [x, y, w, h] = cv2.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 200 and h < 200:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        myList.append(cv2.boundingRect(contour))

        for (x, y, w, h) in myList:

            X1 = x
            Y1 = y
            W1 = w
            H1 = h

            for (x, y, w, h) in myList:

                X2 = x
                Y2 = y
                W2 = w
                H2 = h

            
                if (X1+W1<X2 or X2+W2<X1 or Y1+H1<Y2 or Y2+H2<Y1):
                    print 'No overlap'
                    print ("{} {} {} {}  {} {} {} {}".format(X1, Y1, W1, H1, X2, Y2, W2, H2))
                else:
                    print 'Overlap detected!!!'
                    print ("{} {} {} {}  {} {} {} {}".format(X1, Y1, W1, H1, X2, Y2, W2, H2))
                    
        # show original image with added contours to disk
        #img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('overlap', img)
    #press esc key to stop, any other key to continue
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break
    else:
        continue
    

'''   
        #press esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
'''       

    
cv2.destroyAllWindows()
