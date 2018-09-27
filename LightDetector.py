import numpy as np 
import cv2

def mask_creater(image,lower_color,upper_color):
	lower=np.array(lower_color,dtype="uint8")
	upper=np.array(upper_color,dtype="uint8")

	mask=cv2.inRange(image,lower,upper)
	res=cv2.bitwise_and(image,image,mask=mask)
	return res

cap=cv2.VideoCapture(0)

while(1):
	ret,frame=cap.read()
	blur_img=cv2.medianBlur(frame,3)
	hsv_img=cv2.cvtColor(blur_img, cv2.COLOR_BGR2HSV)
	#lower_white=mask_creater(hsv_img,[0,100,100],[10,255,255])
	lower_white=mask_creater(hsv_img,[0,0,0],[0,0,255])
	#upper_white=mask_creater(hsv_img,[160,100,100],[179,255,255])
	#combined_img=cv2.add(lower_white,upper_white)
	combined_img=lower_white
	
	combined_img=cv2.GaussianBlur(combined_img,(9,9),2,2)
	gray=cv2.cvtColor(combined_img,cv2.COLOR_BGR2GRAY)
	circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,100)

	if circles is None:
		cv2.putText(frame,"Oven os OFF",(10,25),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,255,0),1)
	else:
		cv2.putText(frame,"Oven os ON",(10,25),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,255,0),1)

	cv2.imshow("img",combined_img)
	cv2.imshow("Orignal",frame)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()