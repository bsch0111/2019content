
from PIL import Image
import imagehash

def dHash(file_path):
    hash = imagehash.dhash(Image.open(file_path))
    return hash