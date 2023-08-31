# Mosquitto 

> 모스키토 란?
- 센서와 장치 모바일 기기들간의 연결을 위한 프로토콜
- MQTT 오픈소스로 공개
- ESP32 라즈베리파이 PC 등 통신이 가능한 기기들의 연결을 가능하게 해줌.
- sub(구독자) pub(발행자)로 이루어져 통신을 함.

> 라즈베리 파이 모스키토 실행 (교안 임베디드 iot day2_r1 )
- 환경설정
  - sudo apt install mosquitto
  - sudo apt install mosquitto clients -y
- 테스트 (2개의 터미널 창을열어 각각 입력해 보자)
  - mosquitto_sub -t "everland/animals/tiger" -h 127.0.0.1
  - mosquitto_pub -t "everland/animals/tiger" -h 127.0.0.1 -m aaa
  - 구독자(sub)에서 aaa가 출력 되면 정상.

> PC 환경 테스트
- 주의!!! : cmd창열때 무조건 모스키토 서버 실행  !!! 주의 c폴더-> programfiles -> mosquitto ->에서 cmd창을 열어야함(안그러면 없는 명령어라 나옴)