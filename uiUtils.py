import cv2
import time
fontColor = (50, 50, 50)


class UiUtils:

    def __init__(self):
        self.pTime = 0

   
    def addAngleData(self, frame, angles):
        cv2.putText(frame, f'Little: {round(angles[0], 2)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
        cv2.putText(frame, f'Indicator: {round(angles[1], 2)}', (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
        cv2.putText(frame, f'Middle finger: {round(angles[2], 2)}', (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
        cv2.putText(frame, f'Ring finger: {round(angles[3], 2)}', (20, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
        cv2.putText(frame, f'Thumb finger: {round(angles[4], 2)}', (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, fontColor, 2)
    
    def addFpsData(self, frame):
        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime
        cv2.putText(frame, f'FPS:{int(fps)}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, fontColor, 2)