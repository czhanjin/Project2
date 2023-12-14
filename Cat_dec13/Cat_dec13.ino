#include <Wire.h>
#include <Servo.h>
#include <Adafruit_VL53L0X.h>

const int touchSensorPin = 2;  // Touch sensor
const int servoEar1Pin = 7;       // Servo 1 for ear
const int servoEar2Pin = 8;       // Servo 2 for ear
int servoPin = 3;

const int trigPin = 6;         //  ultrasonic sensor
const int echoPin = 5;         //  ultrasonic sensor

// voltage measurement circuit components
int value = 0;
float voltage;
float R1 = 47000.0;
float R2 = 33000.0;
const int redPin = 9;
const int greenPin = 10;

Servo servoEar1; // servo for ear
Servo servoEar2; // servo for ear
Servo servoArm; // servo for arm 
Servo servoMed;
Adafruit_VL53L0X lox = Adafruit_VL53L0X();
bool isSwitchOn = false;
const int angle_initial = 40;


//int fsrPin = 1;     // the FSR and 10K pulldown are connected to a0
//int fsrReading;     // the analog reading from the FSR resistor divider
//int threshold = 500; // threshold value of the FSR reading to turn LED on/off 

bool earState = false;    // the current state of LED
int lastTouchState;    // the previous state of touch sensor
int currentTouchState; // the current state of touch sensor

void setup() {
  Serial.begin(9600);
  pinMode(touchSensorPin, INPUT);
  currentTouchState = digitalRead(touchSensorPin);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, LOW);

  servoEar1.attach(servoEar1Pin);
  servoEar2.attach(servoEar2Pin);;
  servoEar1.write(90);
  servoEar2.write(90);
  
  if (!lox.begin()) {
    Serial.println(F("Failed to boot VL53L0X"));
    while (1);
  }
  servoMed.attach(13);
  servoMed.write(angle_initial);

  servoArm.attach(servoPin);
  servoArm.write(0);
}

void loop(){
  voltageMeasurement();
  pettingHead();
  medDispenser();
  armWaving();
  // earFlapping();
}


void voltageMeasurement(){
  value = analogRead(A0);
  voltage = value * (5.0/1024)*((R1 + R2)/R2);
  // Serial.print("Voltage =");
  // Serial.println(voltage);
  delay(500);
  
  if (voltage > 8) {
  digitalWrite(greenPin, HIGH);
  digitalWrite(redPin, LOW);
} else {
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, HIGH);
}      
}

void pettingHead(){ 
  lastTouchState    = currentTouchState;             // save the last state
  currentTouchState = digitalRead(touchSensorPin); // read new state
  Serial.print("Current Touch State: ");
  Serial.println(currentTouchState);

  if(lastTouchState == LOW && currentTouchState == HIGH) {
    Serial.println("The sensor is touched");
    earFlapping();
    earFlapping();
  }
}


void earFlapping(){
  servoEar2.write(120);
  servoEar1.write(60);
  delay(500);
  servoEar1.write(90);
  servoEar2.write(90);
  delay(500);
}

void medDispenser(){
VL53L0X_RangingMeasurementData_t measure;
// Perform a distance measurement
  lox.rangingTest(&measure, false);

  if (measure.RangeStatus != 4) {  // Check if measurement is valid
    int distance = measure.RangeMilliMeter;

    if (distance < 80 && distance != 0) {
      servoMed.write(angle_initial+90);
      delay(1000);
      servoMed.write(angle_initial);
      delay(500);
      Serial.print("Distance: ");
      Serial.print(distance);
      Serial.print(" mm, Servo Angle: ");
    } else {
      servoMed.write(angle_initial);
      delay(100);
      // Serial.print("Distance: ");
      // Serial.println(distance);
    }
  }
  delay(100);  
  
}

void armWaving(){
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
  servoArm.write(0);
  delay(500);
  servoArm.write(90);
  delay(500);
  servoArm.write(0);
  delay(500);
  servoArm.write(90);
  delay(500);
  }