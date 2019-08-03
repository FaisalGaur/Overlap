import cv2
import numpy as np
import time

from PIL import ImageGrab
from time import sleep
from PIL import Image
import pytesseract

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

im = np.array(ImageGrab.grab(bbox=None))
showCrosshair = False
fromCenter = False

# Select ROI
r = cv2.selectROI(im, showCrosshair, fromCenter)
print(r)
[x_start, y_start, width, height] = [int(r[0]), int(r[1]), int(r[0] + r[2]), int(r[1] + r[3])]
cv2.destroyAllWindows()


file1 = open("fps.txt","w+")

#Run continuously unless stopped by user
while(1):

    # Select area to capture on screen using X,Y coordinates
    frame = np.array(ImageGrab.grab(bbox=(x_start, y_start, width, height)))

    #Default Format is BGR convert to GRAY
    #grayimage=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #time stamp & file name
    #timestr = time.strftime("%Y%m%d-%H%M%S")
    #filename = "file_%s.png"%timestr

    #Display captured frame
    cv2.imshow('FPS',frame)

    #imgtxt = Image.open(filename)
    fpstxt = pytesseract.image_to_string(frame).encode('utf-8')
    print(fpstxt)

    '''
    file1.write(timestr)
    file1.write("   ")
    file1.write(fpstxt)
    file1.write("\n")  
    '''

    #wait 0.5 seconds (500 ms)
    sleep(0.5)

    #press esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

file1.close()
cv2.destroyAllWindows()
