import numpy as np
import os
import cv2

img=cv2.imread(os.path.join('.','Resources/b.jpg'))
img_edge=cv2.Canny(img,100,200)
img_edge_d=cv2.dilate(img_edge,np.ones((3,3),dtype=np.int8))
img_edge_e=cv2.erode(img_edge_d,np.ones((3,3),dtype=np.int8))
cv2.imshow('Original',img)
cv2.imshow('Edge',img_edge)
cv2.imshow('Edge D',img_edge_d)
cv2.imshow('Edge E',img_edge_e)
cv2.waitKey(0)