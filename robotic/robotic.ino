
#include "Servo.h" 
 
Servo littleFingerServo; 
Servo indicatorFingerServo; 
Servo middleFingerServo; 
Servo ringFingerServo; 
Servo thumbServo; 

int angle = 0; 
 
void setup() { 
    littleFingerServo.attach(4); 
    indicatorFingerServo.attach(5); 
    middleFingerServo.attach(6); 
    ringFingerServo.attach(7); 
    thumbServo.attach(8); 

} 
 
void loop() {
  angle = analogRead(A0); 

  angleSanitized = map(angle, 0, 1023, 0, 179); 
  littleFingerServo.write(angleSanitized); 
  indicatorFingerServo.write(angleSanitized); 
  middleFingerServo.write(angleSanitized); 
  ringFingerServo.write(angleSanitized); 
  thumbServo.write(angleSanitized); 
  
  delay(5);
} 