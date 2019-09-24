from PIL import Image
import imagehash

# 숫자가 0이면 일치하며
# 숫자가 작을수록 비슷하다고 판단
def CPdHash(file1, file2):
    file1_hash = imagehash.dhash(Image.open(file1))
    file2_hash = imagehash.dhash(Image.open(file2))
    return file1_hash - file2_hash