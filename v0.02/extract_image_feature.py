import EXGMS_Feature
import EXORB_Feature
import EXIMS_Feature
import EXdHash_Feature
import hashlib
import numpy as np

def toSha256(pdata):
    hashenc = hashlib.sha256()
    hashenc.update(pdata)
    pText = hashenc.hexdigest()
    return pText

if __name__ == '__main__':

    #img1_path = sys.argv[1]
    #img2_path = sys.argv[2]
    
    img1_path = "./data/0.3THz.jpg"

    pGMS_ListOfKeyPoint = EXGMS_Feature.GMS(img1_path)
    pGMS_data = np.array(pGMS_ListOfKeyPoint)
    pGMS = toSha256(pGMS_data)

    
    pORB_data = EXORB_Feature.ORB(img1_path)
    pORB = toSha256(pORB_data)
    
    pIMS_data = EXIMS_Feature.IMS(img1_path)
    pIMS = toSha256(pIMS_data)

    pdHash = EXdHash_Feature.dHash(img1_path)
    
    #출력은 GMS, ORB, IMS, dHash 순으로 ,에 맞추어 출력
    #stdout으로 출력하고 차후 데이터 베이스화 할때는 csv를 이용한 입력을 이용
    print(pGMS," , ",pORB," , ",pIMS," , ",pdHash)

