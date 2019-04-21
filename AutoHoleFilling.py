# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:24:55 2019

This program takes a simple binary design with "holes" in it and automatically fills the holes using
morphological reconstruction by dilation. In the morphological reconstruction, a marker image and mask is used
@author: eagle
"""

import cv2
import numpy as np

# function for creating the structuring element
def SE(size):
    SE = np.ones((size,size))
    return SE

def formMarkerImg(image):
    iH = image.shape[0] # image height
    iW = image.shape[1] # image width
    
    marker = np.zeros((iH, iW), dtype = 'uint8') # initialize the marker image
    
    # filling the marker image correctly
    for x in range(0, iH):
        for y in range(0, iW):
            if x == 0 or x == (iH - 1) or y == 0 or y == (iW - 1): # if the pixel is on the border
                marker[x, y] = 1 - image[x, y]
            else:
                marker[x, y] = 0
    
    return marker

# function for getting complement of image
def complementImg(image):
    image = cv2.bitwise_not(image)
    return image

# This is where the morphological reconstruction process happens
# n is number of iterations of dilating and bitwise anding
def MorphRecon(marker, mask, SE, n):
    for i in range(0, n):
        dil = cv2.dilate(marker, SE, iterations = 1) # dilate the new marker with structuring element
        result = cv2.bitwise_and(dil, mask) # Bitwise and the dilated image with the mask
        marker = result # update the marker image
    
    return result # after all iterations, return the resulting image of the morphological reconstruction
    
original = cv2.imread("DesignWithHoles2.jpg") # read in image

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY) # convert to grayscale

markerImg = formMarkerImg(gray) # get the marker image

mask = complementImg(gray) # The mask is achieved by getting the complement of the original image

morphReconImg = MorphRecon(markerImg, mask, SE(3), 800) # where the morph recon by dilation happens

result = complementImg(morphReconImg) # Lastly, take the complement of the image from above

# show the output images
cv2.imshow("original", gray) # Original grayscale image
cv2.imshow("result", result) # show the result after complementing morph recon image
cv2.waitKey(0) # If you press enter
cv2.destroyAllWindows() # Close all images being shown