import cv2
import tensorflow
import keras
from PIL import Image, ImageOps
import numpy as np

cascPath = "OpenCV/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('keras_model.h5')
size = (224, 224)

webcam = cv2.VideoCapture(0)
while (True):
    result, image_bgr = webcam.read()
    img_org = image_bgr.copy()
    img_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    faces = faceCascade.detectMultiScale(img_gray)
    for face in faces:
        x, y, w, h = face
        crop_img = Image.fromarray(img_rgb[y:y+h.x:x+h])
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = crop_img
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = model.predict(data)
        print(prediction)
        cv2.rectangle(image_bgr, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('AI FaceDetection', image_bgr)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
webcam.release()
cv2.destroyAllWindows()
