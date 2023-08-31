# 서버로 데이터 전송
// 아래 내용을 git에 올리는 경우 wifi이름과 비번 piv4주소는 가리고 올릴것

- bac를 서버로 전송
- 서버에서 txt를 보내면 우분투에서 받음

> host 찾기
- 내 IP 주소를 찾는다고 생각하면 된다.
  - cmd 창에 ipconfig 를 입력하자
  - 나의 경우 wifi로 연결되어 있는 상태
  ```
  무선 LAN 어댑터 Wi-Fi 2:

   연결별 DNS 접미사. . . . :
   링크-로컬 IPv6 주소 . . . . : fe80::e1ca:e76:df45:8bea%19
   IPv4 주소 . . . . . . . . . : 172.30.1.8
   서브넷 마스크 . . . . . . . : 255.255.255.0
   기본 게이트웨이 . . . . . . : 172.30.1.254
   ```
   - 위의 내용에서 IPv4의 주소가 나의 인터넷 연결 IP 주소라 생각하면된다.



```C
const char* ssid     = "KT_GiGA_2G_Wave2_A1EC";
const char* password = "bcaffzf835";

const char* host = "172.30.1.8";
const char* streamId   = "....................";
```

```C
#include <WiFi.h>

const char* SSID_NAME = "KT_GiGA_2G_Wave2_A1EC"; //와이파이 이름
const char* SSID_PASS = "bcaffzf835";            // 비밀번호
const char* HOST_ADDR = "172.30.1.8";            // ipv4주소 - 주소 값은 cmd 창에서 configip로 확인
const int   HOST_PORT = 6000;

WiFiClient client;    

void setup() {
    Serial.begin(9600);
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(SSID_NAME);
    
    WiFi.begin(SSID_NAME, SSID_PASS);
    
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }    
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());

    delay(1000);
    Serial.print("connecting to ");
    Serial.println(HOST_ADDR);

     if (!client.connect(HOST_ADDR, HOST_PORT)) {
        Serial.println("connection failed");
        return;
    }
}

void loop() {

    // WiFiClient client;
    delay(1000); 
    client.print("bac");    
    while(client.available()) {
        String line = client.readStringUntil('\r');
        Serial.print(line);
    }    
    
}
```

