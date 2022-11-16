#include <ESP32Servo.h>

Servo littleFingerServo;
Servo indicatorFingerServo;
Servo middleFingerServo;
Servo ringFingerServo;
Servo thumbServo;

int angleLittleFinger = 90;
int angleRingFinger = 90;
int angleMiddleFinger = 90;
int angleIndicatorFinger = 90;
int angleThumb = 90;

bool isIncriasing = true;

void setup() {
  Serial.begin(115200);

  thumbServo.attach(27);
  indicatorFingerServo.attach(26);
  middleFingerServo.attach(25);
  littleFingerServo.attach(32);
  ringFingerServo.attach(33);

  littleFingerServo.write(80);
      indicatorFingerServo.write(80);
      middleFingerServo.write(80);
      ringFingerServo.write(80);
      thumbServo.write(80);
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

      angleLittleFinger = firstNumber.toInt() < 90 ? 200 : 90; 
      angleIndicatorFinger =fourthNumber.toInt() < 90 ? 20 : 90;
      angleMiddleFinger = thirdNumber.toInt() < 90 ? 20 : 90;
      angleRingFinger = secondNumber.toInt() < 90 ? 200 : 90; 
      angleThumb = fiveNumber.toInt() < 90 ? 0 : 90;

       //200 abre 90 fech
      littleFingerServo.write(angleLittleFinger);
      //20 abre 90 fecha
      indicatorFingerServo.write(angleIndicatorFinger);
      //20 abre 90 fecha
      middleFingerServo.write(angleMiddleFinger);
      //200 abre 90 fech
      ringFingerServo.write(angleRingFinger);
      //0 abre 90 fecha
      thumbServo.write(angleThumb);
    }
  }

  delay(10);
}