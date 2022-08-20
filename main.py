import cv2
import time
import mediapipe as mp
from roboticHand import RoboticHand

videoPath = "myvideo.mp4"
videoTitle = "Video"
pTime = 0
fontColor = (50, 50, 50)

video = cv2.VideoCapture(videoPath)

mediaPipeHands = mp.solutions.hands
hands = mediaPipeHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

while(video.isOpened()):
    canRead, frame = video.read()
    if not canRead:
        video = cv2.VideoCapture(videoPath)
        canRead, frame = video.read()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, f'FPS:{int(fps)}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, fontColor, 2)

    results = hands.process(frame)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            landsmarks= handLms.landmark
            
            if len(landsmarks) == 21:
                roboticHand = RoboticHand(landsmarks)
                angles = roboticHand.getAngles()
                
                cv2.putText(frame, f'Little: {round(angles[0], 2)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
                cv2.putText(frame, f'Indicator: {round(angles[1], 2)}', (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
                cv2.putText(frame, f'Middle finger: {round(angles[2], 2)}', (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
                cv2.putText(frame, f'Ring finger: {round(angles[3], 2)}', (20, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
                cv2.putText(frame, f'Thumb finger: {round(angles[4], 2)}', (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)

                # This is to customize de dots of connectors
                #for id, lm in enumerate(landsmarks):
                #    h, w, c = frame.shape
                #    cx, cy = int(lm.x *w), int(lm.y*h)
                #    cv2.circle(frame, (cx,cy), 3, (255,0,255), cv2.FILLED)

                mpDraw.draw_landmarks(frame, handLms, mediaPipeHands.HAND_CONNECTIONS)
 
    cv2.imshow(videoTitle,frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()