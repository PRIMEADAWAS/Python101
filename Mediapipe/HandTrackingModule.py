from turtle import position
import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self,
                 static_image_mode=False,
                 max_num_hands=2,
                 model_complexity=1,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):
        self.mode = static_image_mode
        self.maxhands = max_num_hands,
        self.detection_con = min_detection_confidence
        self.tracking_con = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            self.mode, self.maxhands, self.detection_con, self.tracking_con)
        self.mp_draw = mp.solutions.drawing_utils

    def findHands(self, image, draw=True):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)
        if (self.results.multi_hand_landmarks):
            for landmark in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        image, landmark, self.mp_hands.HAND_CONNECTIONS)
        return image

    def findPosition(self, image, handNo=0, draw=True):
        handPosList = []
        if (self.results.multi_hand_landmarks):
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if draw:
                    handPosList.append([id, cx, cy, lm])
        return handPosList


def main():
    wCam, hCam = 1280, 720
    webcamap = cv2.VideoCapture(0)
    webcamap.set(3, wCam)
    webcamap.set(4, hCam)

    pTime = 0

    detector = handDetector()

    while True:
        result, image = webcamap.read()
        image = detector.findHands(image)
        handPosList = detector.findPosition(image)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        image = cv2.flip(image, 1)
        cv2.putText(image, f'FPS:{int(fps)}', (40, 70),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)
        cv2.imshow("HandTracking", image)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

    webcamap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
