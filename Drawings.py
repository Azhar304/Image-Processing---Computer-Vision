import os
import cv2

img=cv2.imread(os.path.join('.','Resources/white.webp'))
print(img.shape)
"""line"""
cv2.line(img,(100,50),(40,20),(255,0,0),5)
"""Rectangle"""
cv2.rectangle(img,(100,50),(40,100),(0,255,0),5)
"""Circle"""
cv2.circle(img,(200,70),50,(0,0,255),-1)
"""Text"""
cv2.putText(img, 'Good Boy',(100,150),cv2.FONT_HERSHEY_PLAIN,3,(210,204,255),3)
cv2.imshow('white',img)
cv2.waitKey(0)

