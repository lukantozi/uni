int buttonState = 0;
int inten = 0;
int slow = 400;
int rapid = 150;
int state = 0;

void setup()
{
  pinMode(2, INPUT);
  // left
  pinMode(11, OUTPUT); // R
  pinMode(10, OUTPUT); // B
  pinMode(9, OUTPUT);  // G
  // right
  pinMode(6, OUTPUT);  // R
  pinMode(5, OUTPUT);  // B
  pinMode(3, OUTPUT);  // G
}

bool waitOrBreak(int ms) {
  for (int i = 0; i < ms; i += 10) {
    if (digitalRead(2) == HIGH) {
      state = !state;
      while (digitalRead(2) == HIGH);
      delay(50);
      return true;
    }
    delay(10);
  }
  return false;
}

void red_left(int intens) {
  analogWrite(11, intens);
  analogWrite(10, 0);
  analogWrite(9, 0);
}

void green_left(int intens) {
  analogWrite(11, 0);
  analogWrite(10, 0);
  analogWrite(9, intens);
}

void blue_left(int intens) {
  analogWrite(11, 0);
  analogWrite(10, intens);
  analogWrite(9, 0);
}

void red_right(int intens) {
  analogWrite(6, intens);
  analogWrite(5, 0);
  analogWrite(3, 0);
}

void green_right(int intens) {
  analogWrite(6, 0);
  analogWrite(5, 0);
  analogWrite(3, intens);
}

void blue_right(int intens) {
  analogWrite(6, 0);
  analogWrite(5, intens);
  analogWrite(3, 0);
}

void slowFade() {
  inten = 255;
  for (int i = 0; i < 5; i++) {
    red_left(inten);
    green_right(inten);
    inten /= 2;
    if (waitOrBreak(slow)) return;
  }
  inten = 255;
  for (int i = 0; i < 5; i++) {
    green_left(inten);
    red_right(inten);
    inten /= 2;
    if (waitOrBreak(slow)) return;
  }
  inten = 255;
  for (int i = 0; i < 5; i++) {
    blue_left(inten);
    red_right(inten);
    inten /= 2;
    if (waitOrBreak(slow)) return;
  }
  inten = 255;
  for (int i = 0; i < 5; i++) {
    green_left(inten);
    blue_right(inten);
    inten /= 2;
    if (waitOrBreak(slow)) return;
  }
}

void rapidBlink() {
  inten = 255;
  for (int i = 0; i < 5; i++) {
    red_left(inten);
    blue_right(inten);
    if (waitOrBreak(rapid)) return;
    red_left(0);
    blue_right(0);
    if (waitOrBreak(rapid)) return;
  }
  for (int i = 0; i < 5; i++) {
    red_right(inten);
    blue_left(inten);
    if (waitOrBreak(rapid)) return;
    red_right(0);
    blue_left(0);
    if (waitOrBreak(rapid)) return;
  }
  for (int i = 0; i < 5; i++) {
    green_right(inten);
    red_left(inten);
    if (waitOrBreak(rapid)) return;
    green_right(0);
    red_left(0);
    if (waitOrBreak(rapid)) return;
  }
  for (int i = 0; i < 5; i++) {
    green_left(inten);
    red_right(inten);
    if (waitOrBreak(rapid)) return;
    green_left(0);
    red_right(0);
    if (waitOrBreak(rapid)) return;
  }
  for (int i = 0; i < 5; i++) {
    blue_left(inten);
    green_right(inten);
    if (waitOrBreak(rapid)) return;
    blue_left(0);
    green_right(0);
    if (waitOrBreak(rapid)) return;
  }
}

void loop() {
  if (state == 0) {
    rapidBlink();
  } else {
    slowFade();
  }
}
