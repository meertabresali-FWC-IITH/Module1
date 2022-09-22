#include <Arduino.h>
// Codes for Distributive laws
// Distributive Law1: X.(Y+Z) = X.Y + X.Z
// Distributive Law2: X+(Y.Z) =(X+Y).(X+Z)

int X;
int Y;
int Z;
int A;
int B;
int C;
int D;

void led(int A, int B, int C, int D)
{
 digitalWrite(5, A);
 digitalWrite(6, B);
 digitalWrite(7, C);
 digitalWrite(8, D);
}

void setup() {
pinMode(2, INPUT); // Manual Input to Arduino
pinMode(3, INPUT); // Manual Input to Arduino
pinMode(4, INPUT); // Manual Input to Arduino

pinMode(5, OUTPUT); // To be conncted to LED1 for LHS of Distributive Law1
pinMode(6, OUTPUT); // To be conncted to LED2 for RHS of Distributive Law1

pinMode(7, OUTPUT); // To be conncted to LED3 for LHS of Distributive Law2
pinMode(8, OUTPUT); // To be conncted to LED4 for RHS of Distributive Law2


}
void loop()
{
  X=digitalRead(2);
  Y=digitalRead(3);
  Z=digitalRead(4);
  
//For Distributive Law1
  A=X&&(Y || Z);      // LHS of Distributive Law1 to be conncted to LED1 for LHS of Distributive Law1
  B=(X&&Y) || (X&&Z); // RHS of Distributive Law1 to be conncted to LED2 for RHS of Distributive Law1
  
//For Distributive Law2
  C=X || (Y&&Z);        // LHS of Distributive Law2 to be conncted to LED3 for LHS of Distributive Law2
  D=(X || Y)&&(X || Z); // RHS of Distributive Law2 to be conncted to LED4 for RHS of Distributive Law2
  
 led(A, B, C, D);

}

