import cv2
import os

img=cv2.imread(os.path.join('.', 'Resources/panda.jpg'))

# colored_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# HSV_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.imshow("Image",img)
# cv2.imshow("Colored Image",colored_img)
# cv2.imshow("HSV_img",HSV_img)
# cv2.imshow("Gray Image",gray_img)
cv2.waitKey(0)