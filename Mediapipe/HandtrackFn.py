import cv2
import mediapipe as mp
import time

wCam, hCam = 1280, 720
webcamap = cv2.VideoCapture(0)
webcamap.set(3, wCam)
webcamap.set(4, hCam)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

pTime = 0

while True:
    result, image = webcamap.read()
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    # print(results.multi_hand_landmarks)
    if (results.multi_hand_landmarks):
        for landmark in results.multi_hand_landmarks:
            # print(landmark.landmark)
            handPosList = []
            for id, lm in enumerate(landmark.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # if(id == 8 or id == 6):
                #     print(id, cx, cy)
                if(id >= 5 and id <= 8):
                    cv2.circle(image, (cx, cy), 8, (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, str(id), (cx, cy),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)
                handPosList.append([id, cx, cy, lm])
            # print(handPosList)
            # print(handPosList[8][3].x)
            if((handPosList[8][2] > handPosList[6][2]) & (handPosList[8][2] < handPosList[0][2])):
                print('index flexion', handPosList[8][2], handPosList[6][2])
            mp_draw.draw_landmarks(image, landmark, mp_hands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # image = cv2.resize(image, (1280, 720))
    # image = cv2.flip(image, 1)
    cv2.putText(image, f'FPS:{int(fps)}', (40, 70),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)
    cv2.imshow("HandTracking", image)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break


webcamap.release()
cv2.destroyAllWindows()
