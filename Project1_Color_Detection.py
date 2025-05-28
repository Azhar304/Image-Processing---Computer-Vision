import cv2
import numpy as np
from PIL import Image

def get_limits(color):
    c=np.uint8([[color]])
    hsv_c=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lower_limit=hsv_c[0][0][0] - 10,100,100
    upper_limit=hsv_c[0][0][0] + 10,255,255

    lower_limit=np.array(lower_limit, dtype=np.uint8)
    upper_limit=np.array(upper_limit, dtype=np.uint8)


    return lower_limit, upper_limit

green=[0,255,0]
cap= cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit=get_limits(color=green)
    mask= cv2.inRange(hsv_img,lower_limit, upper_limit)
    mask_=Image.fromarray(mask)

    bbox=mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2= bbox
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()