import cv2

cap = cv2.VideoCapture("shutter.mp4")

while True:
    ret ,frame = cap.read()
    # if frame:
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

