# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:24:55 2019

@author: eagle
"""

import cv2
import numpy as np

def SE(size):
    SE = np.ones((size,size))
    return SE

def formMarkerImg(image):
    iH = image.shape[0]
    iW = image.shape[1]
    
    marker = np.zeros((iH, iW), dtype = 'uint8')
    
    for x in range(0, iH):
        for y in range(0, iW):
            if x == 0 or x == (iH - 1) or y == 0 or y == (iW - 1):
                marker[x, y] = 1 - image[x, y]
            else:
                marker[x, y] = 0
    
    return marker

def complementImg(image):
    image = cv2.bitwise_not(image)
    return image

# n is number of iterations of dilating and anding
def MorphRecon(marker, mask, SE, n):
    for i in range(0, n):
        dil = cv2.dilate(marker, SE, iterations = 1)
        result = cv2.bitwise_and(dil, mask)
        marker = result
    
    return result
    
original = cv2.imread("DesignWithHoles2.jpg") # read in image

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

markerImg = formMarkerImg(gray)

mask = complementImg(gray)

morphReconImg = MorphRecon(markerImg, mask, SE(3), 800)

result = complementImg(morphReconImg)

# show the output images
cv2.imshow("original", gray) # Original grayscale image
cv2.imshow("result", result)
cv2.waitKey(0) # If you press enter
cv2.destroyAllWindows() # Close all images being shown