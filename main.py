import cv2
import time
from camera import get_camera
from hand_tracker import HandTracker
from predict import predict_gesture
import drone_commands as drone

cap = get_camera()
tracker = HandTracker()

last_command = None
last_time = 0
COOLDOWN = 1.0

while True:
    ret, frame = cap.read()
    landmarks = tracker.process(frame)
    gesture = predict_gesture(landmarks)

    if gesture:
        cv2.putText(frame, f"Gesture: {gesture}", (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        if gesture != last_command and time.time() - last_time > COOLDOWN:
            if gesture == "Takeoff": drone.takeoff()
            elif gesture == "Land": drone.land()
            elif gesture == "Left": drone.move_left()
            elif gesture == "Right": drone.move_right()
            elif gesture == "Up": drone.move_up()
            elif gesture == "Down": drone.move_down()
            elif gesture == "Forward": drone.move_forward()
            elif gesture == "Backward": drone.move_backward()

            last_command = gesture
            last_time = time.time()

    cv2.imshow("Gesture Drone Control", frame)
    key = cv2.waitKey(10) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
