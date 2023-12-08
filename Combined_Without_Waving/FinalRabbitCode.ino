#include <Servo.h>

const int touchSensorPin = 2;  // Touch sensor
const int servo1Pin = 7;       // Servo 1 for ear
const int servo2Pin = 8;       // Servo 2 for ear
//const int servo3Pin = 4;      // Servo 3 for arm
//const int redPin = 9;
//const int greenPin = 10;
//const int bluePin = 11;
const int voltagePin = A0;
const int trigPin = 6;         //  ultrasonic sensor
const int echoPin = 5;         //  ultrasonic sensor
int value = 0;
float voltage;
float R1 = 47000.0;
float R2 = 33000.0;
const int redPin = 9;
const int bluePin = 10;

Servo servo1; // servo for ear
Servo servo2; // servo for ear
//Servo servo3; // servo for arm
Servo myServo;  // servo for ultrasonic sensor
bool isSwitchOn = false;

void setup() {
Serial.begin(9600);
pinMode(touchSensorPin, INPUT);
//pinMode(redPin, OUTPUT);
//pinMode(greenPin, OUTPUT);
//pinMode(bluePin, OUTPUT);
pinMode(voltagePin, INPUT);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);

pinMode(redPin, OUTPUT);
pinMode(bluePin, OUTPUT);
digitalWrite(bluePin, LOW);
digitalWrite(redPin, LOW);

servo1.attach(servo1Pin);
servo2.attach(servo2Pin);
//servo3.attach(servo3Pin);
myServo.attach(13);

servo1.write(90);
servo2.write(90);
myServo.write(0);
//servo3.write(90);


//setColor(0, 0, 0);  // Turn off RGB LED initially
}

void loop() {
 // Code 1 - Touch Sensor Servos
 int touchState = digitalRead(touchSensorPin);
 if (touchState == HIGH) {
   // delay(10);
   if (!isSwitchOn) {
     Serial.println("Switch ON");
     isSwitchOn = true;
     servo1.write(180);
     servo2.write(180);
     //servo3.write(180);
   }
 } else {
   if (isSwitchOn) {
     Serial.println("Switch OFF");
     isSwitchOn = false;
     servo1.write(90);
     servo2.write(90);
     //servo3.write(90);
     delay(100); // Adjust the delay time as needed
     digitalWrite(touchSensorPin, LOW);
   }
 }

// Code 2 - RGB LED
// Green = 0 0 255, Yellow = 185 0 70, Red = (255 0 0)
int sensorValue = analogRead(voltagePin);
float voltage = sensorValue * (9.0 / 1023.0);

value = analogRead(A0);
voltage = value * (5.0/1024)*((R1 + R2)/R2);
Serial.print("Voltage =");
Serial.println(voltage);
delay(500);
if (voltage > 8) {
  digitalWrite(bluePin, HIGH);
  digitalWrite(redPin, LOW);
} else {
  digitalWrite(bluePin, LOW);
  digitalWrite(redPin, HIGH);
}

// Code 3 - Ultrasonic Sensor Servo
long duration, distance;


 digitalWrite(trigPin, LOW);
 delayMicroseconds(2);
 digitalWrite(trigPin, HIGH);
 delayMicroseconds(10);
 digitalWrite(trigPin, LOW);

 duration = pulseIn(echoPin, HIGH);
 distance = (duration / 2) / 29.1;


 if (distance < 6 && distance !=0) {
   //Serial.print(distance);
   //Serial.println(" cm");
   myServo.write(90);  // Rotate the servo to 180 degrees when distance is less than 5 cm
   servo1.write(90);
   servo2.write(90);
   delay(500);
   myServo.write(0);
   if (touchState == HIGH) {
       digitalWrite(touchSensorPin, LOW);
   }
 } else if (distance < 180) {
   //Serial.print(distance);
   //Serial.println(" cm");
   myServo.write(0); 
 }
 delay(500);
}

