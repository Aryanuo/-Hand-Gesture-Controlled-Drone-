import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

class HandTracker:
    def __init__(self):
        self.hands = mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        landmarks = []

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            for lm in hand.landmark:
                landmarks.append((lm.x, lm.y, lm.z))
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        return landmarks
