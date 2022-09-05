#include <Arduino.h>
// Codes for Distributive law
// Distributive Law1: X.(Y+Z) = X.Y + X.Z


int X;
int Y;
int Z;
int A;
int B;


void led(int A, int B)
{
 digitalWrite(5, A);
 digitalWrite(6, B);

}

void setup() {
pinMode(2, INPUT); // Manual Input to Arduino
pinMode(3, INPUT); // Manual Input to Arduino
pinMode(4, INPUT); // Manual Input to Arduino

pinMode(5, OUTPUT); // To be conncted to LED1 for LHS of Distributive Law
pinMode(6, OUTPUT); // To be conncted to LED2 for RHS of Distributive Law


}
void loop()
{
  X=digitalRead(2);
  Y=digitalRead(3);
  Z=digitalRead(4);
  
//For Distributive Law1
  A=X&&(Y || Z);      // LHS of Distributive Law1 to be conncted to LED1 for LHS of Distributive Law
  B=(X&&Y) || (X&&Z); // RHS of Distributive Law1 to be conncted to LED2 for RHS of Distributive Law
  

 led(A, B);
 
}

