# AWS 서버 구축하기

> 기본설정
1. AWS EC2실행후 mobaxterm과 연결
2. 서버 환경 구성

-네트워크 ssafy day1 강의 자료 참고
  
> Echo 프로그램

- Echo 서버 사용자가 무엇을 입력하든 서버가 입력한 데이터를 그대로 되돌려주는 프로그램

- 파일이름 echo_server.c

# 서버 실행하기

- <span style="color:orange">아래의 경우 echo 파일을 실행하는 예시 임.</span> 

> 서버 실행

```
// 1. 빌드
$ gcc echo_server.c o echo_server
// 2. 서버 실행 (port 12345)
$ ./echo_server.c 12345
```
> 클라이언트 실행
- 서버가 실행되면 클라이언트를 생성하여 서버에 접속하게 한다.
- 실행시 13.125.249.48는 내 AWS의 고유 IP주소
- 12345는 포트값(서버와 동일한 포트를 이용해야함) 
```
// 1. 빌드
$ gcc echo_client.c -o echo_client
// 2. 실행 
$ ./echo_client  13.125.249.48 12345
```
> 동작 확인하기 

- 클라이언트에서 hi를 입력
- 클라이언트에서 다시 hi가출력됨.


# 

> NetCat 
- TCP, UDP 네트워크 연결을 통해 데이터를 읽거나 쓸 수 있도록 만든 유틸리티 프로그램

- net cat : network 상에서 사용하는 cat 이며 <span style="color:orange">nc </span> 라고 한다

> NC 테스트

1. 가짜 클라이언트 생성 
   -  $ nc [IP 주소 ] [port]
2. 작성한 서버 실행 
   -  $ ./echo_server 12345
3. 가짜 클라이언트 작동
    - $ nc 127.0.0.1 12345
- 즉 127.0.0.1 : “ 내 컴퓨터 “ 를 의미 . 즉 , aws 서버를 말한다 . 그 서버의 “12345 포트 “ 에 접근하는 것이다

