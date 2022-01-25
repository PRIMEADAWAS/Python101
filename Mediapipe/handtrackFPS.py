import cv2
import mediapipe as mp
import time

webcamap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

pTime = 0

while True:
    result, image = webcamap.read()
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    # print(results.multi_hand_landmarks)
    if (results.multi_hand_landmarks):
        # count = 0
        for landmark in results.multi_hand_landmarks:
            # print((results.multi_handcls_landmarks))
            # count += 1
            mp_draw.draw_landmarks(image, landmark, mp_hands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    image = cv2.resize(image, (1280, 720))
    image = cv2.flip(image, 1)
    cv2.putText(image, f'FPS:{int(fps)}', (40, 80),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 255, 0), 3)
    cv2.imshow("HandTracking", image)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break


webcamap.release()
cv2.destroyAllWindows()
