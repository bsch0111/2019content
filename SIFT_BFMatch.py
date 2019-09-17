#import numpy as np 왜있는지 모르겠음
import cv2
from matplotlib import pyplot as plt
 
img1 = cv2.imread('./sample_base.PNG', 0)
img2 = cv2.imread('./sample_test.PNG', 0)
 
sift = cv2.xfeatures2d.SIFT_create()
 
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
 
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
 
good = []
for m,n in matches:
    if m.distance < 0.3*n.distance:
        good.append([m])
 
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
 
plt.imshow(img3),plt.show()