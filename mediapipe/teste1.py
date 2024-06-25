import mediapipe as mp
import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

mp_hands = mp.solutions.hands.Hands()

videoCap = cv2.VideoCapture(0)
img = videoCap.read()

