import csv
import cv2
from camera import get_camera
from hand_tracker import HandTracker

LABEL = input("Enter gesture label (LEFT / RIGHT / UP etc): ")

cap = cv2.VideoCapture(0)
tracker = HandTracker()

with open("data/gestures.csv", "a", newline="") as f:
    writer = csv.writer(f)

    while True:
        ret, frame = cap.read()
        landmarks = tracker.process(frame)

        if len(landmarks) == 21:
            row = []
            for lm in landmarks:
                row.extend(lm)
            row.append(LABEL)
            writer.writerow(row)
            print("Saved:", LABEL)

        cv2.imshow("Collecting Data", frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
