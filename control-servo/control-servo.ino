#include <Servo.h>
int servoPin = 3;

Servo Servo1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Servo1.attach(servoPin);
  Servo1.write(70);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    int data = Serial.read() - '0';

    switch (data){
      case 1:
        moveServo();
        break;
      default:
        break;
      }
    }

}

void moveServo(){
  Servo1.write(60);
  delay(500);
  Servo1.write(90);
  delay(500);
  Servo1.write(60);
  delay(500);
  Servo1.write(90);
  delay(500);
  }
