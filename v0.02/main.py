import GMS_Feature
import ORB_Feature
import IMS_Feature
import dHash_Feature
import hashlib
import numpy as np


def printFeature():
    print("수정 필요")

def toSha256(pdata):
    hashenc = hashlib.sha256()
    hashenc.update(pdata)
    pText = hashenc.hexdigest()
    return pText

if __name__ == '__main__':

    #img1_path = sys.argv[1]
    #img2_path = sys.argv[2]
    
    img1_path = "./data/0.3THz.jpg"

    pGMS_ListOfKeyPoint = GMS_Feature.GMS(img1_path)
    pGMS_data = np.array(pGMS_ListOfKeyPoint)
    pGMS = toSha256(pGMS_data)

    
    pORB_data = ORB_Feature.ORB(img1_path)
    pORB = toSha256(pORB_data)
    #pIMS = IMS_Feature.IMS(img1_path)
    #pdHash_Signature = dHash_Feature.dHash(img1_path)


    print(pGMS)
    print(pORB)



