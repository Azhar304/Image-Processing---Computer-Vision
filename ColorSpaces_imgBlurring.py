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
cv2.imshow("Image",img)
cv2.imshow("Blurred Image",img_blur)
cv2.waitKey(0)