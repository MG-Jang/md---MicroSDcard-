int sensorPin = A0;
int ledPin = 13;
int sensorPin = 36;    // 36번을 가변저항 가운데 연결 , 36대신 A0로 해도 동일
int sensorValue = 0;  // 초기화

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600)
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(sensorPIn)
  Serial.printin(sensorValue);

  delay(500);
}
