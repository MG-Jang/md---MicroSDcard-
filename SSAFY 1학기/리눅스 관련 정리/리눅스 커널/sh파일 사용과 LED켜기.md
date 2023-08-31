1. 220510-kernel 폴더가 존재한다.
2. mobaxterm 에서 폴더 하나 생성후 파일들을 넣는다.
3. GPIO pin 18번에 LED 연결
4. make 실행
5. $ sudo insmod nobrand.ko 실행
6. LED가 켜지는 것을 볼수 있다.
7. $ sudo rmmod nobrand 실행
8. LED 꺼짐

- 이때 alias.sh파일이 왜존재하냐?
  - 결론: sudo insmod nobrand.ko, sudo rmmod nobrand 실행하기가 <br> 너무 길기 때문에 sc , sd 로 켜고 끄기 위해

9. $ source ./alias.sh  입력 -> sh이 실행됨
10. $ sc 
11. $ sd
12. 입력해보자  // sc sd는 강사님이 임의로 정한것이므로 딱히 의미는 없다.
13. LED가 깜빡 거린다.

14. app을 실행시켜보자
- $ sudo mknod /dev/nobrand c 100 0
- $ sudo chmod 666 /dev/nobrand   
- 를 입력 
15. sc
16. ./app
17. 실행하면 오류가 안뜨는 것을 알 수 있다.