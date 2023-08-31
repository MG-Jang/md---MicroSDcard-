# ESP32

> 왜 ESP32 를 사용할까??
- 정답: 싸게 센서의 값을 보내기 위해
- 라즈베리파이, stm32, arduino Uno 로도 가능하다. 하지만 비용이 많이 듬.
- 따라서 통신을 위한 전용 칩을 사용

> 동작

LED 점등
- digital output: 외부 LED 점등
- digital iniput : 외부 키 입력 받기
- uart tx : PC 로 데이터 보내기
- uart rx : 단문자 받기 , 문자열 받기
  - 도전: 1on, 1off, 2on, 2off 입력받아서 각각의 led 제어해보기
- analog 입력 받기 : led dimming
  - 도전: vr 입력받아서 led 밝기 조절하기
- analog 출력 하기 : pwm


LED 점등 하기
```C
#define LED_1_PIN 17
#define LED_2_PIN 16

#define INTERVAL 100

void setup() {
  // put your setup code here, to run once:
    pinMode(LED_1_PIN, OUTPUT);
    pinMode(LED_2_PIN, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_1_PIN,LOW);
  digitalWrite(LED_2_PIN,HIGH);
  delay(INTERVAL);
  
  digitalWrite(LED_1_PIN,HIGH);
  digitalWrite(LED_2_PIN,LOW);
  delay(INTERVAL);
}
```

가변저항
```C
int sensorPin = 36;    // 36번을 가변저항 가운데 연결 , 36대신 A0로 해도 동일
int sensorValue = 0;  // 초기화

void setup() {
  // declare the ledPin as an OUTPUT:
  Serial.begin(9600);  //보드 레이트
}

void loop() {
  // read the value from the sensor:
  int sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);   // print문 뒤에 ln 붙는거 확인
  delay(500);
}
```

```C
#include <WiFi.h>
#include "packet.h"

const char* SSID_NAME = "KT_GiGA_2G_Wave2_A1EC";
const char* SSID_PASS = "bcaffzf835";
const char* HOST_IP   = "172.30.1.14";*
const int   HOST_PORT = 6001;
int tx_count= 0; 
WiFiClient client;

packet_t tx_packet;
char tx_buf[128]= {0, };

void setup() {
    Serial.begin(9600);
    delay(10);

    // 일단 공유기와 접속을 해야 한다.
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(SSID_NAME);
    WiFi.begin(SSID_NAME, SSID_PASS);

    // 공유기와 접속 못하면 영구 대기, .... 이 계속 시리얼 모니터로 출력된다.
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    // 공유기와 연결되면 아래 코드를 탄다.
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.print("IP address: "); // 할당 받은 IP, 서버 IP가 아님!
    Serial.println(WiFi.localIP());

    // 서버와 접속 시도 한다.
    Serial.print("Connecting to ");
    Serial.print(HOST_IP);
    Serial.print(':');
    Serial.println(HOST_PORT);    
    
    // 접속이 성공, 실패 하면?
    if (!client.connect(HOST_IP, HOST_PORT)) {
        Serial.println("Connection failed"); // 서버 접속 실패
        return;
    }
    else {
        Serial.println("Connection Success !!"); // 서버와 접속 성공!
    }
    
    tx_packet.uid = 222;
    tx_packet.temp=  22;
    tx_packet.humi=  22;
    tx_packet.volt=  22;
    tx_packet.amp =  22;
    
}

void loop() {

    if (client.connected()) {
        /*
        Serial.println("sending data to server");      
        //client.write(0x02);
        client.print("B");
        client.print(tx_packet.uid);
        client.print(",");
        client.print(tx_packet.temp);
        client.print(",");
        client.print(tx_packet.humi);
        client.print(",");
        client.print(tx_packet.volt);
        client.print(",");
        client.print(tx_packet.amp);
        client.print("E");
        //client.write(0x0D);
        //client.write(0x0A);
        //client.write(0x03);
        client.flush();
        */

        sprintf(tx_buf, "%d,%d,%d,%d,%d", tx_packet.uid, tx_packet.temp, tx_packet.humi, tx_packet.volt, tx_packet.amp);
        client.print(tx_buf);
        client.flush();
    
    }
    else {
      Serial.println("Connection failed"); // 서버 접속 실패
    }
    // Read all the lines of the reply from server and print them to Serial
    while(client.available()) {
        String line = client.readStringUntil('\r');
        Serial.print(line);
    }
    delay(1000);    
}
```

- 데이터 보는 법 우측 상단 +돋보기 표시 누르면됨