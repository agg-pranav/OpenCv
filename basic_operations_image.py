import numpy as np
import cv2

img = cv2.imread('saic_logo.jpg',-1)

 
# print(img.shape)
# print(img.size)
# print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# adding two images
# cv2.addWeighted(img, alpha,img2, beta ,scalar)



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()