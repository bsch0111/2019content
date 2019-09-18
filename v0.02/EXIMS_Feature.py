from image_match.goldberg import ImageSignature

def IMS(file_path):

    gls = ImageSignature()
    img1_gls = gls.generate_signature(file_path)

    return img1_gls