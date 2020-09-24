import cv2
import datetime

cap = cv2.VideoCapture("shutter.mp4")
# Getting video properties
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
cap.set(4,3000)

# Adding text/date&time to video
while True:
    ret ,frame = cap.read()
    if ret == True:
        font = cv2.FONT_ITALIC
        text = 'Width: '+ str(cap.get(3)) + " Height: "+ str(cap.get(4))
        date_t = str(datetime.datetime.now())
        frame = cv2.putText(frame,date_t,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
