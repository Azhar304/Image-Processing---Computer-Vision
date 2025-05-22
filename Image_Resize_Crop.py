import os
import cv2

img=cv2.imread(os.path.join('.', 'Resources/panda.jpg'))

#image resizing
# resized_img=cv2.resize(img,(510,255))
#
# print(img.shape)
# print(resized_img.shape)
#
# cv2.imshow("Image",img)
# cv2.imshow("Resized Image",resized_img)
# cv2.waitKey(0)

#image Cropping

print(img.shape)
cropped_img=img[150:450,250:550]
cv2.imshow("Image",img)
cv2.imshow("Cropped Image",cropped_img)
cv2.waitKey(0)