# root 계정 연결 및 사용자 비밀번호 변경

```
참고
서버관리자: 직접 root로 접속할 일없다. 있으면 sudo 사용
임베디드개발자: 다른 유저 없음. 무조건 root로 개발 그러므로 sudo라는 명령어를 쓸일도 없다.
```

```
!매우 중요한 내용
임베디드리눅스에서는 다음과 같이 동작되도록 한다
1. 켜자마자 바로 root 로 자동 로그인 되도록 한다
2. 자동으로 세탁기 App 을실행하도록 만든다.

즉 , 켜자마자 root 권한으로 자동 App 실행
```

<br> 

> 사용자 비밀번호 변경
> 
|명령어|의미|
|---|---|
|passwd|현재 사용자 패스워드 변경<br>* sudo가 안붙는 이유:<br> (사용자가 자신의 비밀번호정도는 변경 가능하도록 되어있음)|
|sudo passwd 사용자| 사용자 패스워드를 변경 |
|sudo passwd |<span style="color:orange">(절대 쓰지 말것)</span> root 패스워드를 변경<br> -> 보안상 치명적인 문제가 발생할 수 있음 |

<br> 
<br> 

> root로 접근

|명령어|의미|
|---|---|
|sudo su| @앞이 root로 변경되며 root로 들어감|
```
이때 sudo 로 들어갈 수 있는것은 메인 계정만 가능. 그래서 해커가 해킹을 하는 경우 root의 비번은 관리자도 모르기때문에 sudo 접근이 가능한 메인 계정을 공략
따라서 main계정은 이름을 메인 게정인것처럼 만들면 안됨.
```
|sudo usermod -aG sudo [username]| username도 root에 접근 가능하도록 권한을 부여함 |
|---|---|

<br> 
<br> 

> "$"의미
```
$는 일반 유저를 의미
#은 root를 의미
따라서# 이 붙어있는 명령어는 앞에 sudo를 붙이면됨
```

>시간 설정 (시스템 로그 메세지 시간 정확히 찍으려고 Host 기본 세팅)

|명령어|의미|
|---|---|
|sudo apt install rdate| rdate(remote date)멀링 있는 서버에서 받아옴|
|sudo rdate time.bora.net| lg유플러스가 운영하는 서버 시간|

> 유저 추가 및 삭제
```
user를 추가하면 cd /home/ 에 사용자가 추가됨
여기서 ls -al 을 입력하면 group과 user usergroup other 의 write read excute를 확인가능
```

|명령어|의미|
|---|---|
|sudo adduser [사용자]| 사용자를 추가|
| su [사용자] | switch 사용자|
| exit | 메인 사용자로 돌아감(이미 메인 사용자면 사용자 종료)| 
```
! 주의 GUI 상에서 exit은 터미널 창끄기고MObaX에서는 사용자가 로그아웃이됨
 또한 접속을 끊을때는 exit을 해야함 그렇지않고 서버를 꺼버리면
다른 사용자까지 꺼지게됨
```
|||
|---|---|
|sudo deluser [사용자]| 사용자를 제거(하지만 잔류 폴더등이 남음)|
|sudo deluser [사용자] --remove-all-files| 완전히 깔금하게 사용자를 제거|

> 그룹 생성 및 사용자 추가

|명령어|의미|
|---|---|
|cat /etc/passwd| 명령어로 사용자 확인|
|cat /etc/group| 명령어로 그룹 확인|
|groups|자신이 속한 그룹 확인|
|sudo addgroup [그룹명]|그룹을 추가|
|sudo gpasswd -a [사용자명] [그룹명]| 사용자를 그룹에 추가|
|sudo gpasswd -d [사용자명] [그룹명]| 사용자를 그룹에 제거|
<br>
> 권한 생성 및 추가

|명령어|의미|
|---|---|
|ls -al| 권한확인|
```
이때 맨 앞부분 한글자는 파일의 종류
•--: 레귤러
•d: 디렉토리
•l: link 윈도우의 바로가기 파일
•c or b: 장치파일
```

|||
|---|---|
|cat /etc/group| 명령어로 그룹 확인|
|groups|자신이 속한 그룹 확인|
|sudo addgroup [그룹명]|그룹을 추가|
|sudo gpasswd -a [사용자명] [그룹명]| 사용자를 그룹에 추가|
|sudo gpasswd -d [사용자명] [그룹명]| 사용자를 그룹에 제거|

> owner 변경
- owner user와 group 변경: chwon [User이름]:[Group이름]  [파일명]


> 모드 변경

|||
|---|----|
|chmod u+r ./[파일명]|user 에 r 권한 추가|
|chmod o-w ./[파일명]|other 에 w 권한 제외|
|chmod a+w ./[파일명]|a : all<br> u,g,o 모두 w 권한 추가|