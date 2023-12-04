# https://github.com/JiHyun-Jo7/CV2/blob/main/README.md#21-teseract-

import numpy as np
import cv2
from PIL import Image
import pytesseract

filename = 'letter02.jpg'
img = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img)
text = pytesseract.image_to_string(img, lang='kor+eng')
print(text)
