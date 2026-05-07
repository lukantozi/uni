#include <Wire.h>
#include <Adafruit_LiquidCrystal.h>
#include <Servo.h>

const int PIN_LDR = A0;
const int PIN_POT = A1;
const int PIN_BTN = 2;
const int PIN_RGB_R = 3;
const int PIN_RGB_G = 5;
const int PIN_RGB_B = 6;
const int PIN_LED = 13;
const int PIN_BUZZ  = 8;
const int PIN_SERVO = 9;

Adafruit_LiquidCrystal lcd(0);
Servo lockServo;

bool armed = false;
bool alarming = false;
bool lastBtn = HIGH;
unsigned long lastDebounce = 0;
unsigned long alarmStart = 0;
unsigned long msgShowUntil = 0; // replaces delay() for status messages

void setRGB(int r, int g, int b) {
  analogWrite(PIN_RGB_R, r);
  analogWrite(PIN_RGB_G, g);
  analogWrite(PIN_RGB_B, b);
}

void setup() {
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_RGB_R, OUTPUT);
  pinMode(PIN_RGB_G, OUTPUT);
  pinMode(PIN_RGB_B, OUTPUT);
  pinMode(PIN_BUZZ, OUTPUT);
  pinMode(PIN_BTN, INPUT_PULLUP);

  lockServo.attach(PIN_SERVO);
  lockServo.write(0);

  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Security Station");
  lcd.setCursor(0, 1);
  lcd.print("  Press BTN...  ");
  delay(2000);
  lcd.clear();

  setRGB(0, 0, 120);
}

void loop() {
  int ldr = analogRead(PIN_LDR);
  int pot = analogRead(PIN_POT);
  unsigned long now = millis();

  // arm/disarm
  bool btn = digitalRead(PIN_BTN);
  if (btn == LOW && lastBtn == HIGH && now - lastDebounce > 50) {
    armed = !armed;
    alarming = false;
    lastDebounce = now;
    digitalWrite(PIN_BUZZ, LOW);
    digitalWrite(PIN_LED,  LOW);
    lcd.clear();

    if (armed) {
      lockServo.write(0);
      setRGB(200, 0, 0);
      lcd.setCursor(0, 0);
      lcd.print("** ARMED **     ");
      lcd.setCursor(0, 1);
      lcd.print("Lock: CLOSED    ");
    } else {
      lockServo.write(90);
      setRGB(0, 200, 0);
      lcd.setCursor(0, 0);
      lcd.print("DISARMED        ");
      lcd.setCursor(0, 1);
      lcd.print("Lock: OPEN      ");
    }
    msgShowUntil = now + 1000;  // show message for 1s, non-blocking
  }
  lastBtn = btn;

  // don't overwrite the armed/disarmed message for 1 second
  if (now < msgShowUntil) {
    delay(200);
    return;
  }

  // armed: intrusion detection
  if (armed && !alarming) {
    int threshold = map(pot, 0, 1023, 50, 650);

    if (ldr < threshold) {
      alarming = true;
      alarmStart = now;
      lcd.clear();
      lcd.setCursor(0, 0); lcd.print("!! INTRUDER !!  ");
      lcd.setCursor(0, 1); lcd.print("ALARM TRIGGERED ");
    } else {
      lcd.setCursor(0, 0);
      lcd.print("Armed | LDR:");
      lcd.print(ldr);
      lcd.print("    ");
      lcd.setCursor(0, 1);
      lcd.print("Sens.:");
      lcd.print(threshold);
      lcd.print("        ");
    }
  }

  // alarm
  if (alarming) {
    bool beat = (now / 300) % 2;
    digitalWrite(PIN_LED,  beat);
    digitalWrite(PIN_BUZZ, beat);
    if (beat) setRGB(255, 0, 0);
    else setRGB(0,   0, 0);

    if (now - alarmStart > 10000) {
      alarming = false;
      digitalWrite(PIN_BUZZ, LOW);
      lcd.clear();
      lcd.setCursor(0, 0); lcd.print("Alarm reset.    ");
      lcd.setCursor(0, 1); lcd.print("Still ARMED.    ");
      msgShowUntil = now + 1500;
    }
  }

  // idle
  if (!armed && !alarming) {
    digitalWrite(PIN_LED,  LOW);
    digitalWrite(PIN_BUZZ, LOW);
    lockServo.write(90);

    int t = (now / 8) % 256;
    int blue = t < 128 ? t * 2 : (255 - t) * 2;
    setRGB(0, 0, blue);

    lcd.setCursor(0, 0); lcd.print("STANDBY         ");
    lcd.setCursor(0, 1);
    lcd.print("LDR:");
    lcd.print(ldr);
    lcd.print(" POT:");
    lcd.print(pot);
    lcd.print("  ");
  }

  delay(100);
}
