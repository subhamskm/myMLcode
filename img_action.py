#!/usr/bin/python3

import cv2
img=cv2.imread("dog.jpeg")
cv2.line(img,(0,0),(161,78),(0,0,225),4)
cv2.rectangle(img,(120,9),(255,125),(0,67,225),3)
cv2.circle(img,(161,78),10,(255,255,255),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"DOGGG",(10,100),font,1,(0,0,0),4,cv2.LINE_AA)
cv2.imshow("lineimg",img)
cv2.waitKey(0)

