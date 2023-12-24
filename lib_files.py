import cv2
from PIL import Image
import pytesseract


img_file="test_img.png"

img=Image.open(img_file)
print(img)
img.show()