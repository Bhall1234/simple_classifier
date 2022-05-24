import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.spatial import distance

im = np.array(Image.open('test.jpeg').convert('L').resize((200,130))) #you can pass multiple arguments in single line

grey_image = Image.fromarray(im).save('test_grey.png')
    
image = Image.open("test_grey.png")

data = np.asarray(image)

# Image 2
im2 = np.array(Image.open('test2.jpeg').convert('L').resize((200,130))) #you can pass multiple arguments in single line

grey_image2 = Image.fromarray(im2).save('test_grey2.png')
    
image2 = Image.open("test_grey2.png")

data2 = np.asarray(image2)


def EDM(A,B):
    p1 = np.sum(A**2, axis = 1) [:, np.newaxis]
    p2 = np.sum(B**2, axis = 1) 
    p3 = -2 * np.dot(A,B.T)
    #return np.round(np.sqrt(p1+p2+p3),2)
    #print(distance.euclidean(point1,point2))
    print(np.round(np.sqrt(p1+p2+p3),2))

EDM(data, data2)

#print(distance.euclidean(data,data2))