//setup code just the pins, functions and a small test

#include <Servo.h>

Servo turningServo;

const int maxSpeed = 60;
const int minSpeed = 0;

void turn(int pos){
  const int midPoint = 90;
  const int range = 45;
  
  pos = constrain(pos, midPoint-range, midPoint+range);
  turningServo.write(pos);
  }

void drive(int mspeed, int mode){
  mspeed = constrain(mspeed, minSpeed, maxSpeed);
  analogWrite(4, mspeed); // set speed

  if (mode == 3){
    digitalWrite(D5, 0);    // forward
    digitalWrite(D3, 1);
    }
  else if (mode == 2){
    digitalWrite(D5, 1);    // backward
    digitalWrite(D3, 0);
    }
  else if (mode == 1){
    digitalWrite(D5, 0);    // glide
    digitalWrite(D3, 0);
    }
  else{
    digitalWrite(D5, 1);    // brake
    digitalWrite(D3, 1);
    }
  }

void setup() {
    turningServo.attach(2);
    pinMode(D3, OUTPUT);   // digital 0 to 1
    pinMode(D4, OUTPUT);   // PWM 0 to 255
    pinMode(D5, OUTPUT);   // digital 0 to 1
    
    pinMode(LEDB, OUTPUT); // onboard LED on if LOW
}

void loop() {
  
  digitalWrite(LEDB, 0);//on
  turn(90);
  delay(500);
  drive(100, 3);
  delay(500);
  drive(0, 0);
  delay(500);
  drive(100, 2);
  delay(500);
  drive(0, 0);
  delay(500);
  turn(90);
  delay(500);
  turn(45);
  delay(500);
  turn(135);
  delay(500);
  turn(90);
  digitalWrite(LEDB, 1);//off
  delay(2000);



}
