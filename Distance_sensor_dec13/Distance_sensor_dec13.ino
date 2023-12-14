#include <Wire.h>
#include <Servo.h>
#include <Adafruit_VL53L0X.h>

Servo servoMed;  // Added semicolon here
Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
  Serial.begin(9600);

  if (!lox.begin()) {
    Serial.println(F("Failed to boot VL53L0X"));
    while (1);
  }

  servoMed.attach(13);
  servoMed.write(0);
}

void loop() {
  VL53L0X_RangingMeasurementData_t measure;

  // Perform a distance measurement
  lox.rangingTest(&measure, false);

  if (measure.RangeStatus != 4) {  // Check if measurement is valid
    int distance = measure.RangeMilliMeter;

    if (distance < 60 && distance != 0) {
      servoMed.write(90);
      delay(1000);
      servoMed.write(0);
      delay(500);
      Serial.print("Distance: ");
      Serial.print(distance);
      Serial.print(" mm, Servo Angle: ");
    } else {
      servoMed.write(0);
      delay(100);
      Serial.println(distance);
    }
  }
  delay(100);  // Add a delay to avoid rapid changes
}  
