import cv2
import numpy as np
from straug.process import Invert
from PIL import Image

# Image Processing for Pixelate Image
no = 86
image = cv2.imread(f'test_result/DataTest{no}_rlt.png')

# Convert the image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
binary_image = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imwrite(f"DataTest{no}_rlt.png",binary_image)


# Result Show
'''
cv2.imshow('hasil',binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''