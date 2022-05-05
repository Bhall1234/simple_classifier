import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = 'test.png'
img = cv2.imread(img_path, 0) # read image as grayscale. Set second parameter to 1 if rgb is required
plt.show()