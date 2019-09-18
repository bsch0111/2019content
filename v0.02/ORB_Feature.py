import cv2

def ORB(file_path):
    img1 = cv2.imread(file_path, 0)
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)

    return des1