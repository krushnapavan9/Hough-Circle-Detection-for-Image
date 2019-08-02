
import numpy as np
import cv2 as cv

gray = cv.imread('Image path')

output=gray.copy()
gray1=gray.copy()
        
gray1 = cv.cvtColor(gray1,cv.COLOR_BGR2GRAY)
	gray1 = cv.GaussianBlur(gray1,(5,5),0);
gray1 = cv.medianBlur(gray1,5)

gray1 = cv.adaptiveThreshold(gray1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,3.5)
kernel = np.ones((3,3),np.uint8)
gray1 = cv.erode(gray1,kernel,iterations = 1)
	
gray1 = cv.dilate(gray1,kernel,iterations = 1)

circles1 = cv.HoughCircles(gray1, cv.HOUGH_GRADIENT, 1, 20, param1=73, param2=76, minRadius=0, maxRadius=0)

circles1 = np.uint16(np.around(circles1))

for i in circles1[0,:]:    
    cv.circle(output,(i[0]-8,i[1]),i[2]+5,(0,255,0),2)

frame = cv.resize(output, (900,500))
cv.imshow('detected circles',frame)
cv.waitKey(0)
cv.destroyAllWindows()
