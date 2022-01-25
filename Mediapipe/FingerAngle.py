import cv2
import mediapipe as mp
import time
import numpy as np
import math
from numpy import (dot, arccos, clip)
from numpy.linalg import norm


wCam, hCam = 1280, 720
webcamap = cv2.VideoCapture(0)
webcamap.set(3, wCam)
webcamap.set(4, hCam)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

pTime = 0
handPosList = []
finger = ["Thumb", "Index", "MIddle", "Ring", "little"]
while True:
    result, image = webcamap.read()
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if (results.multi_hand_landmarks):
        for landmark in results.multi_hand_landmarks:
            handPosList = []
            for id, lm in enumerate(landmark.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                handPosList.append([id, cx, cy, lm])
                # if(id > 4 and id < 9):
                #     cv2.circle(image, (cx, cy), 8, (236, 208, 154), cv2.FILLED)
                #     cv2.putText(image, str(id), (cx, cy),
                #                 cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (161, 114, 21), 2)

            for i in range(5):
                x1, y1 = handPosList[i*4+1][1], handPosList[i*4+1][2]
                x2, y2 = handPosList[i*4+2][1], handPosList[i*4+2][2]
                x3, y3 = handPosList[i*4+3][1], handPosList[i*4+3][2]
                u = [x1-x2, y1-y2]
                v = [x3-x2, y3-y2]
                c = dot(u, v)/norm(u)/norm(v)  # -> cosine of the angle
                angle = arccos(clip(c, -1, 1))  # if you really want the angle
                degree = angle * 180 / math.pi
                # print(degree)
                if(degree < 135):
                    # print('Index flexion :', degree)
                    cv2.circle(image, (x1, y1), 15,
                               (236, 208, 154), cv2.FILLED)
                    cv2.putText(image, " " + finger[i] + " Finger", (x1, y1),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (81, 187, 250), 1)

            mp_draw.draw_landmarks(image, landmark, mp_hands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # image = cv2.resize(image, (1280, 720))

    cv2.putText(image, f'FPS:{int(fps)}', (40, 70),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)
    cv2.imshow("HandTracking", image)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break


webcamap.release()
cv2.destroyAllWindows()
