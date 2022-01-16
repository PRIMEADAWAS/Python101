import cv2

imagePath = 'image/people.jpg'
cascPath = "OpenCV/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
# print(faceCascade)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(gray)

faces = faceCascade.detectMultiScale(gray)
# print(faces)

# x, y, w, h = faces[3]
# print(x, y, w, h)
# cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 12)

print(f'There are {len(faces)} faces found.')

for face in faces:
    x, y, w, h = face
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 12)


# show img
imgresize = cv2.resize(image, (900, 600))
cv2.imshow('AI FaceDetection', imgresize)
cv2.waitKey(0)
cv2.destroyAllwindow()
