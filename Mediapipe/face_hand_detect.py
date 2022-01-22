import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

with mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results_face = face_detection.process(image_rgb)
        results_hand = hands.process(image_rgb)

        # Draw the face detection annotations on the image.
        image.flags.writeable = True
        if results_face.detections:
            for detection in results_face.detections:
                mp_drawing.draw_detection(image, detection)

        # Draw the hand annotations on the image.
        if results_hand.multi_hand_landmarks:
            for hand_landmarks in results_hand.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        image = cv2.resize(image, (1280, 720))
        cv2.imshow('Face & Hand Detection', cv2.flip(image, 1))
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

cap.release()
cv2.destroyAllWindows()
