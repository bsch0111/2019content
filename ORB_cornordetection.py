import numpy as np
import cv2
 
filename = './data/1THz.jpg'
img = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
img2 = None
 
orb = cv2.ORB_create()
kp, des = orb.detectAndCompute(img, None)
 
img2 = cv2.drawKeypoints(img, kp, None, (255,0,0), flags=0)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()