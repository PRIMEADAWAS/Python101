import cv2
cap = cv2.VideoCapture('image/seawave.mp4')
# use webcam
# cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    result, frame = cap.read()
    if result == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Title', gray)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
