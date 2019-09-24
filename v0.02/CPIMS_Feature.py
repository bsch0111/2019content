import pandas
from image_match.goldberg import ImageSignature


def CPIMS(file1, file2):
    gis = ImageSignature()

    a = gis.generate_signature(file1)
    b = gis.generate_signature(file2)
    c = gis.normalized_distance(a,b)

    data = [[c]]
    result_data=pandas.DataFrame(data, columns=['  IMS normalized_distance'])

    return result_data