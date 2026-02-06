# ✋ Hand Gesture Controlled Drone (MediaPipe + MLP)

This project implements a **real-time hand gesture–based control system** using a webcam.  
Hand gestures are detected live and converted into **drone movement commands** such as takeoff, land, left, right, up, down, forward, and backward.

The project combines **Computer Vision + Machine Learning** using:
- **OpenCV** for camera input
- **MediaPipe** for hand landmark detection
- **MLP (Multi-Layer Perceptron)** for gesture classification

> ⚠️ Currently, drone commands are implemented as **dummy functions (print statements)**.  
> The code structure is ready for integration with a real drone SDK (e.g., DJI Tello).

---

## 🧠 How the System Works (Simple Overview)

Webcam
↓
OpenCV captures video frames
↓
MediaPipe detects hand & 21 landmarks
↓
MLP model classifies the gesture
↓
Gesture mapped to drone command


Instead of working on raw image pixels, the system uses **hand landmarks**, which makes it:
- Robust to background changes
- Less sensitive to lighting
- Easier and faster to train

---

## ✋ Supported Gestures & Commands

| Gesture | Command |
|------|------|
| ✋ Open palm | Takeoff |
| ✊ Closed fist | Land |
| 👈 Thumb left | Move Left |
| 👉 Thumb right | Move Right |
| 👍 Thumb up | Move Up |
| 👎 Thumb down | Move Down |
|     Index finger upward| Move Forward |
|     Two finger upward| Move Backward |

👉 Thumb-only gestures are used for motion commands(up,down,left,right) to reduce confusion.

---

## 📁 Project Structure

hand_gesture_drone/
│
├── camera.py # Opens the webcam using OpenCV
├── hand_tracker.py # MediaPipe hand landmark detection
├── data_collector.py # Collects labeled training data
├── train_mlp.py # Trains the MLP classifier
├── predict.py # Loads model and predicts gestures
├── drone_commands.py # Dummy drone command functions
├── main.py # Runs the live gesture control system
│
├── data/
│ └── gestures.csv # Collected gesture dataset
│
├── models/
│ ├── gesture_mlp.pkl # Trained MLP model
│ └── label_encoder.pkl # Label encoder
│
├── requirements.txt
└── README.md


---

## 🛠️ Requirements

- Python **3.10**
- A working webcam
- Virtual environment (recommended)

### Required Python Libraries

All dependencies are listed in `requirements.txt`:
- opencv-python
- mediapipe
- numpy
- pandas
- scikit-learn
- joblib

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/hand-gesture-drone.git
cd hand-gesture-drone

2️⃣ Install dependencies
pip install -r requirements.txt
📊 Step 1: Collect Gesture Data
Run the data collection script:

python data_collector.py
How it works:

Enter a gesture label (e.g., LEFT)

Hold the gesture in front of the camera for 3–5 seconds

Multiple samples are automatically recorded (one per frame)

Press q to stop

Repeat for all gestures

The data is saved to:

data/gestures.csv
🧠 Step 2: Train the Model
Train the MLP gesture classifier:

python train_mlp.py
This step:

Reads gestures.csv

Trains an MLP neural network

Prints evaluation metrics:

Accuracy

Confusion Matrix

Precision, Recall, F1-score

Saves trained files to:

models/
🔁 Re-run this step only when the dataset changes.

▶️ Step 3: Run the Live Gesture Control System
Start real-time gesture recognition:

python main.py
What happens:

Webcam window opens

Hand landmarks are drawn

Predicted gesture is displayed

Corresponding drone command is printed

Press q or ESC to exit


🧪 Typical Workflow
First-time setup:
data_collector.py → train_mlp.py → main.py
Adding new gestures later:
data_collector.py → train_mlp.py → main.py
Daily demo / testing:
main.py only
