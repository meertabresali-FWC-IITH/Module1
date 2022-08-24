#include <Arduino.h>
// Program for Distributive law X.(Y+Z) = X.Y + X.Z

int X;
int Y;
int Z;
int A;
int B;

void setup() {
pinMode(2, INPUT); // Manual Input to Arduino
pinMode(3, INPUT); // Manual Input to Arduino
pinMode(4, INPUT); // Manual Input to Arduino

pinMode(5, OUTPUT); // To be conncted to LED1
pinMode(6, OUTPUT); // To be conncted to LED2

}
void loop()
{
  X=digitalRead(2);
  Y=digitalRead(3);
  Z=digitalRead(4);

  A=X&&(Y || Z);
  

  B=(X&&Y) || (X&&Z);
 
 digitalWrite(5, A);
 digitalWrite(6, B);

}

