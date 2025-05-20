import cv2

# img=cv2.imread('Resources/panda.jpg')
#
# cv2.imshow('panda',img)
# cv2.waitKey(1000)

framewidth=360
frameheight=240
# capture=cv2.VideoCapture("Resources/test.mp4") downloaded video playing
capture=cv2.VideoCapture(0) #for webcam\
capture.set(3,framewidth)
capture.set(4,frameheight)

while(True):
    success,img=capture.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1)& 0xff==ord('q'):
        break