import cv2

import mediapipe as mp
from roboticHand import RoboticHand
from uiUtils import UiUtils
import json

file = open('./config.json')
jsonData = json.load(file)

if (jsonData['usesCellphoneCapture']):
    video = cv2.VideoCapture(jsonData['phoneIp'])
else:
    video = cv2.VideoCapture(jsonData['videoPath'])


mediaPipeHands = mp.solutions.hands
hands = mediaPipeHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
ui = UiUtils()

while video.isOpened():
    canRead, frame = video.read()
    if not canRead:
        video = cv2.VideoCapture(jsonData['videoPath'])
        canRead, frame = video.read()

    ui.addFpsData(frame)
   
    results = hands.process(frame)

    if results.multi_hand_landmarks:
       
        for handLms in results.multi_hand_landmarks:
           
            landsmarks= handLms.landmark
            
            if len(landsmarks) == 21:
                roboticHand = RoboticHand(landsmarks)
                angles = roboticHand.getAngles()
                
                ui.addAngleData(frame, angles)

                mpDraw.draw_landmarks(frame, handLms, mediaPipeHands.HAND_CONNECTIONS)
 
    cv2.imshow("Eyes of the and",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()