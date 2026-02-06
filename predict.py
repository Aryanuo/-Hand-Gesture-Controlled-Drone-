import numpy as np
import joblib

model = joblib.load("models/gesture_mlp.pkl")
encoder = joblib.load("models/label_encoder.pkl")

def predict_gesture(landmarks):
    if len(landmarks) != 21:
        return None

    features = np.array(landmarks).flatten().reshape(1, -1)
    pred = model.predict(features)[0]
    return encoder.inverse_transform([pred])[0]
