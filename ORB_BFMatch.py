# import numpy as np 예제에는 있지만 왜 있는지 모르겠음
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('./sample_base.PNG', 0)
img2 = cv2.imread('./sample_test.PNG', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)

matches = sorted(matches, key = lambda x:x.distance)


img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=2)
plt.imshow(img3),plt.show()