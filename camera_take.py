#!/usr/bin/python3

import cv2
cam=cv2.VideoCapture(0)
if cam.isOpened():
    print("Camera is ready to take picture..")
    status, frame = cam.read()
    cv2.imshow("frame1",frame)
    cv2.waitKey(0)
    #.imwrite("myimage.jpeg",frame)
    cam.release()
else:
    print("Check your camera drivers..")
