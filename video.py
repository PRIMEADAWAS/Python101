import cv2
cap = cv2.VideoCapture('image/seawave.mp4')
# use webcam
# cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    result, frame = cap.read()
    if result == True:
        cv2.imshow('Title', frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
