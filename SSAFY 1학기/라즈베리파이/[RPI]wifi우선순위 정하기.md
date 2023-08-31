# RPI 와이파이 우선순위 정하기

- 라즈베리를 사용하다보면 원하지 않는 wifi에 먼저 연결되어 moba 또는VNC를 사용하는데 어려움이 있다. 따라서 이를 해결하기위해 wifi연결 우선 순위를 정해준다.

> 실행 방법
1. 라즈베리파이 cmd창을 연후 아래와 같이 입력한다.
```
$ sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
```
2. network 파일중 자신이 원하는 파일안에 priority=[우선순위] 를 넣는다. (참고사이트 참고)
   - ex) priority=1
3. 저장후 닫는다.
4. 정상적으로 실행되는 것을 확인한다.(만약 우선순위가 뒤에있는 wifi가 연결되더라도 우선순위 앞에 있는 wifi를 발견하면 자동으로 그 wifi로 연결한다.)

> 참고사이트: 
- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=lovespreads&logNo=221196996613