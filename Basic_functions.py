import cv2
path="Resources/panda.jpg"
img=cv2.imread(path)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(21,21),0)
imgcanny=cv2.Canny(imgblur,50,50)

# cv2.imshow("panda",img)
# cv2.imshow("gray",imggray)
cv2.imshow("blur",imgblur)
cv2.imshow("canny",imgcanny)

cv2.waitKey(1000)
