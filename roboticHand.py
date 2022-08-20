from vector import Vector
from roboticFinger import RoboticFinger
from utils import Utils
class RoboticHand:
    
    
    def __init__(self, data):
        self.data = data
        self.setUp()

    def setUp(self):
        littleFinger = RoboticFinger(self.data[17], self.data[18], self.data[20])
        indicatorFinger = RoboticFinger(self.data[13], self.data[14], self.data[16])
        middleFinger = RoboticFinger(self.data[9], self.data[10], self.data[12])
        ringFinger = RoboticFinger(self.data[5], self.data[6], self.data[8])
        thumb = RoboticFinger(self.data[1], self.data[2], self.data[4])


        angle = littleFinger.getAngleOfFinger()
       
        print(Utils.toDegrees(angle))


       

        


        