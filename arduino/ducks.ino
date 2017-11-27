void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  char a = 0;
  if (Serial.available()) {
    a = Serial.read();

    if(a == '0') {
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
    } else if(a == '1') {
        digitalWrite(2, HIGH);
        digitalWrite(3, LOW);
    } else if(a == '2') {
        digitalWrite(2, LOW);
        digitalWrite(3, HIGH);
    } else if(a == '3') {
        digitalWrite(2, HIGH);
        digitalWrite(3, HIGH);
    }
  }
}
