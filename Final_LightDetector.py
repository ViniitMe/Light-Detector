import cv2
import numpy as np 
import datetime
import time

cap=cv2.VideoCapture(0)

while(1):
	ret,frame=cap.read()
	
	#Pretext 
	text="Light is OFF"
	
	#Image Processing
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	blur_img=cv2.GaussianBlur(gray,(11,11),0)

        #if pixel value<252 make everything black else white
	thresh_img=cv2.threshold(blur_img,252,255,cv2.THRESH_BINARY)[1]
	thresh_img=cv2.erode(thresh_img,None,iterations=2)
	thresh_img=cv2.dilate(thresh_img,None,iterations=4)

	img,contours,hierarchy=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnt=contours
	for c in cnt:
		(x,y,w,h)=cv2.boundingRect(c)
		cv2.rectangle(thresh_img,(x,y),(x+w,y+h),(255,0,0),1)
		text="Light is ON"

	cv2.putText(frame,"{}".format(text),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
	circles=cv2.HoughCircles(thresh_img,cv2.HOUGH_GRADIENT,1.2,100)

	cv2.imshow("img",thresh_img)
	cv2.imshow("orig_img",frame)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
