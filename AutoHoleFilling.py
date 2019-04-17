# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:24:55 2019

@author: eagle
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def strucuringElement():
    SE = np.ones((3,3))
    return SE

def formMarkerImg(image):
    iH = image.shape[0]
    iW = image.shape[1]
    
    marker = np.zeros((iH, iW))
    
    for x in range(0, iH):
        for y in range(0, iW):
            if x == 0 or x == (iH - 1) or y == 0 or y == (iW - 1):
                marker[x, y] = 1 - image[x, y]
            else:
                marker[x, y] = 0
    
    return marker

def formMask(image):
    image = cv2.bitwise_not(image)
    return image

def MorphRecon():
    
original = cv2.imread("DesignWithHoles.jpg") # read in image
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY) # get grayscale of image