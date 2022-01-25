import cv2
cap = cv2.VideoCapture(0)
while (True):
    result, frame = cap.read()
    cv2.imshow('Title', frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
cap.release()
cv2.destroyAllWindows()
