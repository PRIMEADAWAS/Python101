import cv2

cascPath = "OpenCV/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

webcam = cv2.VideoCapture(0)

while (True):
    result, image = webcam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('AI FaceDetection', image)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

webcam.release()
cv2.destroyAllWindows()
