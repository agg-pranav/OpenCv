import numpy as np
import cv2

# img = cv2.imread('saic_logo.jpg',1)

# Adding image using numpy
img = np.zeros([512,512,3],np.uint8)

# Drawing line
img = cv2.line(img,(0,0),(255,255),(27,22,25),10)
img = cv2.arrowedLine(img,(255,0),(255,255),(100,22,25),10) # Arrowed line


# Drawing Rectangle
img = cv2.rectangle(img,(0,255),(30, 299),(124,45,85),9)

# Drawing Circle
# img = cv2.circle()

# Adding Text
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'SAIC',(255,255),font,4,(120,120,0),9,cv2.LINE_4)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()