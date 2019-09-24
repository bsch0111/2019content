import pandas
import cv2

def CPORB(file1, file2):
    img1 = cv2.imread(file1, 0)
    img2 = cv2.imread(file2, 0)

    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1,des2)

    matches = sorted(matches, key = lambda x:x.distance)


    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=2)
    
    #plt.imshow(img3),plt.show()
    
    data = [[len(kp1),len(kp2),len(matches)]]
    result_data=pandas.DataFrame(data, columns=['Image1_feature','Image2_feature','match_feature'])

    return result_data