
#include "Servo.h"

Servo littleFingerServo;
Servo indicatorFingerServo;
Servo middleFingerServo;
Servo ringFingerServo;
Servo thumbServo;

int angleLittleFinger = 0;
int angleRingFinger = 0;
int angleMiddleFinger = 0;
int angleIndicatorFinger = 0;
int angleThumb = 0;

void setup() {
  Serial.begin(9600);

  littleFingerServo.attach(4);
  indicatorFingerServo.attach(5);
  middleFingerServo.attach(6);
  ringFingerServo.attach(7);
  thumbServo.attach(8);

}

int sanitizeValue(String value) {
  int angle = value.toInt();
  if (angle < 0) {
    angle = 0;
  } else if (angle > 179) {
    angle = 179;
  }
  return angle;
}

void loop() {
  if (Serial.available() > 0) {
    String buffered = Serial.readString();

    if (buffered.length() > 5) {

      int indexOfFirstWord = buffered.indexOf('/');
      String message = buffered.substring(0, indexOfFirstWord);

      int delimiter1 = message.indexOf(";");
      int delimiter2 = message.indexOf(";", delimiter1 + 1);
      int delimiter3 = message.indexOf(";", delimiter2 + 1);
      int delimiter4 = message.indexOf(";", delimiter3 + 1);
      int delimiter5 = message.indexOf(";", delimiter4 + 1);

      String firstNumber = message.substring(0, delimiter1);
      String secondNumber = message.substring(delimiter1 + 1, delimiter2);
      String thirdNumber = message.substring(delimiter2 + 1, delimiter3);
      String fourthNumber = message.substring(delimiter3 + 1, delimiter4);
      String fiveNumber = message.substring(delimiter4 + 1, delimiter5);

      angleLittleFinger = sanitizeValue(firstNumber);
      angleIndicatorFinger = sanitizeValue(secondNumber);
      angleMiddleFinger = sanitizeValue(thirdNumber);
      angleRingFinger = sanitizeValue(fourthNumber);
      angleThumb = sanitizeValue(fiveNumber);
    }
  }

  littleFingerServo.write(angleLittleFinger);
  //indicatorFingerServo.write(angleIndicatorFinger);
  //middleFingerServo.write(angleMiddleFinger);
  //ringFingerServo.write(angleRingFinger);
  //thumbServo.write(angleThumb);


}
