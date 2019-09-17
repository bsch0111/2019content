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