import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays

#image = Image.open("test.png")


im = np.array(Image.open('test.jpeg').convert('L')) #you can pass multiple arguments in single line
#print(type(im))

grey_image = Image.fromarray(im).save('gr_kolala.png')
    
image = Image.open("gr_kolala.png")

data = np.asarray(image)
    #print(type(data))
    #print(data.shape)
image2 = Image.fromarray(data)
    #print(type(image2))

    #print (image2)
    #print (image2.size)

# Image 2
im2 = np.array(Image.open('test.jpeg').convert('L')) #you can pass multiple arguments in single line

grey_image2 = Image.fromarray(im2).save('test_grey2.png')
    
image2 = Image.open("test_grey2.png")

data2 = np.asarray(image2)

image4 = Image.fromarray(data2)

#print(data2)

def EDM(A,B):
    p1 = np.sum(A**2, axis = 1) [:, np.newaxis]
    p2 = np.sum(B**2, axis=1) 
    p3 = -2 * np.dot(A,B.T)
    #return np.round(np.sqrt(p1+p2+p3),2)
    print(np.round(np.sqrt(p1+p2+p3),2))

EDM(data, data2)