

//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

//    Can be client or even host   //
#ifndef STASSID
#define STASSID "Tabrez"  // Replace with your network credentials
#define STAPSK  "12345678"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;


void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}

//-------------------------------------------------------//

#include <Arduino.h>
// Codes for Distributive laws
// Distributive Law1: X.(Y+Z) = X.Y + X.Z


int X;
int Y;
int Z;

int A;
int B;


void led(int A, int B)
{
 digitalWrite(15, A);
 digitalWrite(16, B);

}
void setup() {
pinMode(2, INPUT); // Manual Input to Arduino
pinMode(4, INPUT); // Manual Input to Arduino
pinMode(5, INPUT); // Manual Input to Arduino

pinMode(15, OUTPUT); // To be conncted to LED1 for LHS of Distributive Law
pinMode(16, OUTPUT); // To be conncted to LED2 for RHS of Distributive Law

}

void loop()
{
  X=digitalRead(2);
  Y=digitalRead(4);
  Z=digitalRead(5);
  
//For Distributive Law1
  A=X&&(Y || Z);      // LHS of Distributive Law to be conncted to LED1 for LHS of Distributive Law
  B=(X&&Y) || (X&&Z); // RHS of Distributive Law to be conncted to LED2 for RHS of Distributive Law

  
 led(A, B);

}
