from vector import Vector

class RoboticFinger:
    def __init__(self, firstPoint, secondPoint, thirdPoint):
        aVector = Vector(firstPoint.x, firstPoint.y)
        bVector = Vector(secondPoint.x, secondPoint.y)
        cVector = Vector(thirdPoint.x, thirdPoint.y)

        self.firstJoint = aVector.copy().sub(bVector)
        self.secondJoint = bVector.copy().sub(cVector)

    def getAngleOfFinger(self):
        return self.firstJoint.angleBetweenLine(self.secondJoint)