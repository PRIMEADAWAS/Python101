import cv2
import mediapipe as mp


webcamap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
    result, image = webcamap.read()
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    # print(results.multi_hand_landmarks)
    if (results.multi_hand_landmarks):
        for landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, landmark, mp_hands.HAND_CONNECTIONS)
    image = cv2.resize(image, (1280, 720))
    cv2.imshow("HandTracking", image)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break


webcamap.release()
cv2.destroyAllWindows()
