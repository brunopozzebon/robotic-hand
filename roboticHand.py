from vector import Vector
from roboticFinger import RoboticFinger
from utils import Utils

class RoboticHand:
    
    
    def __init__(self, data):
        self.data = data
        self.littleFinger = RoboticFinger(self.data[17], self.data[18], self.data[20])
        self.indicatorFinger = RoboticFinger(self.data[13], self.data[14], self.data[16])
        self.middleFinger = RoboticFinger(self.data[9], self.data[10], self.data[12])
        self.ringFinger = RoboticFinger(self.data[5], self.data[6], self.data[8])
        self.thumb = RoboticFinger(self.data[1], self.data[2], self.data[4])
       
    def getAngles(self):
        littleFingerAngle = self.littleFinger.getAngleOfFinger()
        indicatorFingerAngle = self.indicatorFinger.getAngleOfFinger()
        middleFingerAngle = self.middleFinger.getAngleOfFinger()
        ringFingerAngle = self.ringFinger.getAngleOfFinger()
        thumbAngle = self.thumb.getAngleOfFinger()

        return [
            Utils.toDegrees(littleFingerAngle),
            Utils.toDegrees(indicatorFingerAngle),
            Utils.toDegrees(middleFingerAngle),
            Utils.toDegrees(ringFingerAngle),
            Utils.toDegrees(thumbAngle),
        ]
