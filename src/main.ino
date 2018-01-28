#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const int dispenserPins[] = {5, 6, 9, 10, 11};
float drinks[4];
boolean dispenserRunning[4];
unsigned long motorStartMillis[4];
unsigned long motorRunMillis[4];

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  Serial.println("Ready");

  // initialize the LCD
	lcd.init();

	// Turn on the blacklight and print a message.
	lcd.backlight();
	lcd.print("system is operational!");

  // Assign pins as output
  for (int a = 0; a < 5; a++) {
    pinMode(dispenserPins[a], OUTPUT);
    dispenserRunning[a] = false;

  }
}

void loop() {

  while (Serial.available() > 0) {
    String incomingData = Serial.readString();

    for (int a = 0; a < 5; a++) {
      String drinkString[a] = getValue(incomingData, ',', a);
      drinks[a] = drinkString[a].toFloat();
      motorRunMillis[a] = map(drinks[a], 0, 1, 0, 10000);
    }
  }

  for (int a = 0; a < 5; a++) {
    if (motorRunMillis[a] > 0) {
      digitalWrite(dispenserPins[a], HIGH);
      motorStartMillis[a] = millis();
      dispenserRunning[a] = true;
    }

    if (dispenserRunning[a] && (millis() - motorStartMillis[a] > motorRunMillis)) {
      digitalWrite(dispenserPins[a], LOW);
      dispenserRunning[a] = false;
    }

  }

}

// The function below grabs a string, and separates it into constituents with a delimiter.

String getValue(String data, char separator, int index) {
 int found = 0;
 int strIndex[] = {0, -1};
 int maxIndex = data.length()-1;

 for (int i=0; i <= maxIndex && found <= index; i++) {
   if (data.charAt(i) == separator || i == maxIndex) {
       found ++;
       strIndex[0] = strIndex[1]+1;
       strIndex[1] = (i == maxIndex) ? i+1 : i;
   }
 }

 return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}
