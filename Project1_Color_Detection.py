import cv2
import numpy as np
from PIL import Image

def get_limit(color):
    c =np.uint8([[color]])
    hsv_c= cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit = hsv_c [0][0][0] - 5, 100 , 100
    lower_limit=np.array(lower_limit, dtype=np.uint8)

    upper_limit = hsv_c [0][0][0] + 5, 255 , 255
    upper_limit=np.array(upper_limit, dtype= np.uint8)


    return lower_limit, upper_limit

""""Multiple object color detection"""
colors = {
    'green': ([0, 255, 0], (0, 255, 0)),
    'blue': ([255, 0, 0], (255, 0, 0)),
    'yellow': ([0, 255, 255], (0, 255, 255)),
}

capture= cv2.VideoCapture(0)
while True:
    ret, frame= capture.read()
    """Conversion to rsv color frma for easier detection"""
    hsv_image= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    """Applying mask """
    for name, (bgr, draw_color) in colors.items():
        lower_limit, upper_limit=get_limit(bgr)
        mask=cv2.inRange(hsv_image, lower_limit, upper_limit)
        mask_=Image.fromarray(mask)
        bbox= mask_.getbbox()
        if bbox is not None:
            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame,(x1,y1),(x2,y2),draw_color,2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
"""Single Clor object detection"""
# green=[0,255,0]
# cap= cv2.VideoCapture(0)
# while True:
#     ret, frame=cap.read()
#     hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     lower_limit, upper_limit=get_limits(color=green)
#     mask= cv2.inRange(hsv_img,lower_limit, upper_limit)
#     mask_=Image.fromarray(mask)
#
#     bbox=mask_.getbbox()
#     if bbox is not None:
#         x1, y1, x2, y2= bbox
#         frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
#
#     cv2.imshow('frame',frame)
#
#     if cv2.waitKey(1) & 0xff==ord('q'):
#         break

