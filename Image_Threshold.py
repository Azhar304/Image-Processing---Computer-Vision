import cv2
import os

img= cv2.imread(os.path.join('.','Resources/Bear.jpg'))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh= cv2.threshold(img_gray, 88,255, cv2.THRESH_BINARY)
thresh=cv2.blur(thresh,(20,20))
ret, thresh= cv2.threshold(img_gray, 88,255, cv2.THRESH_BINARY)
cv2.imshow("Gray image",img)
cv2.imshow("Thresh",thresh)

cv2.waitKey(0)