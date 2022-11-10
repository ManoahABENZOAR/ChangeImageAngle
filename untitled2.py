#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:42:20 2022

@author: cytech
"""

import numpy as np
import cv2

img = cv2.imread("p (1).jpg")

height, width, _ = img.shape


cv2.imshow('input', img)


cv2.waitKey(0)

"""
pts1 = np.float32([[176,187],[465,94],[98, 411],[572,356]])
pts2 = np.float32([[100,200],[500,200],[100,700],[500, 700]])
"""

pts1 = np.float32([[134,117],[298,193],[56,497],[230,479]])
pts2 = np.float32([[100,120],[270,124],[100,500],[270, 504]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img, M, (340, 740))

cv2.imshow('output',dst)
cv2.waitKey(0)


cv2.destroyAllWindows()
