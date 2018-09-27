import cv2
import numpy as np 
 
cap = cv2.VideoCapture(0) 
 
while(1):       
    ret, frame = cap.read() 
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_bl = np.array([110,50,50])
    upper_bl = np.array([130,255,255])
 
	# Here we are defining range of bluecolor in HSV
	# This creates a mask of blue coloured 
	# objects found in the frame.
    mask = cv2.inRange(hsv, lower_bl, upper_bl)
 
	# The bitwise and of the frame and mask is done so 
	# that only the blue coloured objects are highlighted 
	# and stored in res
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
 
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()