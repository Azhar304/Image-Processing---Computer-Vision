import cv2
import os
"""Color Spacing"""
# img=cv2.imread(os.path.join('.', 'Resources/panda.jpg'))
img=cv2.imread(os.path.join('.', 'Resources/Person.webp'))
# colored_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# HSV_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# cv2.imshow("Colored Image",colored_img)
# cv2.imshow("HSV_img",HSV_img)
# cv2.imshow("Gray Image",gray_img)

"""Image Blurring"""
k_size=7
img_blur=cv2.blur(img, (k_size, k_size))
"""Gaussian Blurring"""
img_gaussian=cv2.GaussianBlur(img, (k_size, k_size), 3)
"""Median blur"""
img_median=cv2.medianBlur(img, k_size)

cv2.imshow("Image",img)
# cv2.imshow("Blurred Image",img_blur)
# cv2.imshow("Gaussian Blur",img_gaussian)
cv2.imshow("Median Blur",img_median)

cv2.waitKey(0)