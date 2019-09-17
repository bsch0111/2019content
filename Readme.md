# 1. 이미지 유사도 모듈 개발

image_compare.py

## GMS 모듈개발

    ### 입력 데이터
    
    (1) Photography
    
    - Terahertz Image, Hyperspectral Image
    - 입력 데이터 조건
        - 데이터 확장자
        - 데이터 크기
        - 데이터 고려조건 : 아직 없음, 추후 뽑아내야함
    
    - 특성 추출 기술
        - 코너 기반 추출(GMS)
        - 이미지 해시 기반 추출(pHash)
    
    - 예상 결과값
        - 특성 정보 (유사개수 비교그림중일치특징점/기준그림전체특징점)
        - 내부 요철 및 손상흔적
        - 표면과 다른 밑그림 흔적

    GMS 기반 특성정보 추출
    github 홈페이지 : https://github.com/JiawangBian/GMS-Feature-Matcher
    
    
    python 라이브러리
    mathEnum
    cv2.ocl.setUseOpenCL
    numpy
    
    morgan 피씨에서 실행
    pip install cv2를 실행해야함
    에러 : ERROR: Could not find a version that satisfies the requirement cv2 (from versions: none)
    해결 방법 1: pip3 install opencv-python
    해결 방법 2: chmod +755 gms_matcher.py 실행
    해결 방법 3: #!/usr/bin/python 첫줄에 추가
    그러다가 갑자기 python3 ./python/gms_matcher.py가 됨
    
    결과
    Found 1180 matches 
    X Server는 실행되지 않음
    
    해야할 일
    A 그림과 B 그림의 특징점 개수를 추출할 수 있을까
    
    GMS 특징점 개수 추출
    
    mask, num_inliers = self.get_inlier_mask(False, False)
            print('Found', num_inliers, 'matches')
    

    get_inlier_mask 정의
    
    def get_inlier_mask(self, with_scale, with_rotation):
            max_inlier = 0
            self.set_scale(0)
    
            if not with_scale and not with_rotation:
                max_inlier = self.run(1)
                return self.inlier_mask, max_inlier
            elif with_scale and with_rotation:
                vb_inliers = []
                for scale in range(5):
                    self.set_scale(scale)
                    for rotation_type in range(1, 9):
                        num_inlier = self.run(rotation_type)
                        if num_inlier > max_inlier:
                            vb_inliers = self.inlier_mask
                            max_inlier = num_inlier
    
                if vb_inliers != []:
                    return vb_inliers, max_inlier
                else:
                    return self.inlier_mask, max_inlier
            elif with_rotation and not with_scale:
                vb_inliers = []
                for rotation_type in range(1, 9):
                    num_inlier = self.run(rotation_type)
                    if num_inlier > max_inlier:
                        vb_inliers = self.inlier_mask
                        max_inlier = num_inlier
    
                if vb_inliers != []:
                    return vb_inliers, max_inlier
                else:
                    return self.inlier_mask, max_inlier
            else:
                vb_inliers = []
                for scale in range(5):
                    self.set_scale(scale)
                    num_inlier = self.run(1)
                    if num_inlier > max_inlier:
                        vb_inliers = self.inlier_mask
                        max_inlier = num_inlier
    
                if vb_inliers != []:
                    return vb_inliers, max_inlier
                else:
                    return self.inlier_mask, max_inlier

GMS 이미지 유사도 결과 출력

라이브러리 pandas : python 테이블 추가

pip3 install pandas

    import pandas
    '''
    data = [[len(self.keypoints_image1),len(self.keypoints_image2),len(all_matches)]]
            result_data=pandas.DataFrame(data, columns=['Image1_feature','Image2_feature','match_feature'])
    
            print(result_data)

## pHash 모듈 개발

pip3 install image_match

pip3 install scipy

pip3 install numpy

    import pandas
    from image_match.goldberg import ImageSignature
    
    gis = ImageSignature()
    
    a = gis.generate_signature("./data/test2.jpg")
    b = gis.generate_signature("./data/0.28THz.jpg")
    d = gis.generate_signature("./s1.PNG")
    c = gis.normalized_distance(a,b)
    
    
    data = [[c]]
    result_data=pandas.DataFrame(data, columns=['     A&B normalized_distance'])
    
    print(result_data)

python3 image_compare.py A.jpg B.jpg