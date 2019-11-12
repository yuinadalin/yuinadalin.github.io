# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import os.path
import numpy as np 
import PIL

   

directory = os.path.dirname(os.path.abspath(__file__)) 

filename = os.path.join(directory, 'amalfi.jpg')

img = plt.imread(filename)
  

height = len(img)
width = len(img[0])
for row in range(0, 1067):
    for column in range(0, 30):
        img[row][column] = [255, 0, 255]
        
height = len(img)
width = len(img[0])
for row in range(0, 30):
    for column in range(0, 1600):
        img[row][column] = [255, 0, 255]

        
height = len(img)
width = len(img[0])
for row in range(0, 1067):
    for column in range(1570, 1600):
        img[row][column] = [255, 0, 255]
        
height = len(img)
width = len(img[0])
for row in range(1037, 1067):
    for column in range(0, 1600):
        img[row][column] = [255, 0, 255]
        
img2 = PIL.Image.fromarray(img)

new_img = img2.rotate(180, expand=True)


fig, ax = plt.subplots(1, 1)

ax.imshow(new_img, interpolation='none')

fig.show()

