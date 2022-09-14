// To verify Distributive Law of Boolean Algebra on the LEDs Using AVR-GCC

// Distributive law is expressed by X.(Y+Z) = XY+XZ

// Inputs are X, Y, Z and Outputs are A (for LHS) and B (for RHS)

// LHS = X.(Y+Z) is given to LED1 and RHS = XY+XZ is given to LED2

// Both LEDS (LED1 and LED2) are identified at same level for random input variables (X, Y and Z)

#include <avr/io.h>

#include <util/delay.h>

#include <stdbool.h>

int main (void)
{
bool A, B, X, Y, Z;

DDRD = 0b00000000; 	// 2, 3, 4 pins as input
PORTD= 0b00011100;
DDRB = 0b00000011;  	// 8 and 9 pins as output

 while(1) 
 {
  	X = (PIND & (1<<PIND2)) == (1<<PIND2);	
	Y = (PIND & (1<<PIND3)) == (1<<PIND3);
	Z = (PIND & (1<<PIND4)) == (1<<PIND4);
	   
A= X & (Y | Z); 	// LHS of Distributive Law
B= (X&Y) | (X&Z); 	// RHS of Distributive Law
  

PORTB |=(A<<0);		// LHS is given to Pin 8 and from there to LED1
PORTB |=(B<<1);		// RHS is given to Pin 9 and from there to LED2

}
return 0;

}
