#!/usr/bin/python3

import cv2
img=cv2.imread("dog.jpeg",0)
print(img.shape)
cv2.imshow('Dogg',img)
cv2.waitKey(0)
cv2.imwrite('blacknwhite.jpeg',img)
