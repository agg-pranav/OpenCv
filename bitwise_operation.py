import cv2
import numpy as np

img1 = np.zeros((500,500,3),np.uint8)
img1 = cv2.rectangle(img1,(250,0),(500,500),(255,255,255),-1)

img2 = np.zeros((500,500,3),np.uint8)
img2 = cv2.rectangle(img2,(200,0),(300,250),(255,255,255),-1)

bitAnd = cv2.bitwise_and(img2,img1)
bitOr = cv2.bitwise_or(img2,img1)
bitXor = cv2.bitwise_xor(img2,img1)
bitNot2 = cv2.bitwise_not(img2)
bitNot1 = cv2.bitwise_not(img1)

cv2.imshow('1',img1)
cv2.imshow('2',img2)


cv2.waitKey(0)
cv2.destroyAllWindows()