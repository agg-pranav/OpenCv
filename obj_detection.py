import numpy as np
import cv2
def nothing(x):
    pass

cap = cv2.VideoCapture('shutter.mp4')

cv2.namedWindow('Tracker')
cv2.createTrackbar('LH','Tracker',0,255,nothing)
cv2.createTrackbar('UH','Tracker',255,255,nothing)=cv2.createTrackbar('LS','Tracker',0,255,nothing)
cv2.createTrackbar('US','Tracker',255,255,nothing)
cv2.createTrackbar('LV','Tracker',0,255,nothing)
cv2.createTrackbar('UV','Tracker',255,255,nothing)

while True:
    # img = cv2.imread('balls.webp')
    _, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH','Tracker')
    l_s = cv2.getTrackbarPos('LS','Tracker')
    l_v = cv2.getTrackbarPos('LV','Tracker')

    u_h = cv2.getTrackbarPos('UH','Tracker')
    u_s = cv2.getTrackbarPos('US','Tracker')
    u_v = cv2.getTrackbarPos('UV','Tracker')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('result',res)
    cv2.imshow('original',img)
    cv2.imshow('mask',mask)

    key  = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()