# 쉘 명령어 정리

<br>

|명령어(코드)|용도|예시|
|---|---|---|
|#|주석처리|#주석입니다.|
|@echo "문자열";| echo출력 안됨, 문자열만 출력| @echo "hello";|
|의존성타겟: 타겟 타겟|HA를 실행하면 HI HO의 내용 출력(HA는 의존성 타겟)| HA: HI HO|
|매크로이름 = "문자열"| 매크로 이름과 내용 설정|MSG = "test" |
|@echo $(MSG);| MSG매크로 출력<span style="color:orange"> (띄어쓰기 주의!!)</span>|@echo $(MSG);|
|매크로 += "문자열"|기존 매크로 뒤에 내용이 붙음(자동 띄어쓰기가됨)|MSG += "yellow"|
|매크로 := $(기존 매크로)|현재까지 저장된 기존 매크로가 출력됨|<img src = "./Linux img/smaple1.JPG" width = 200><br>SIMPLE 출력: OH , RECUL 출력: OH GOOD KFC|
|$@|현재 자신의 target이름 출력( 오른쪽 출력 결과 ok)|ok: <br> @echo "$@" |
<br>

<span style="color:orange"> 단! 매크로의 경우 맨위에 써주는 것이 가독성이 좋다.</span>
- <span style="color:orange"> 이유: </span><br>
<img src = "./Linux img/예시1.JPG" width = 200>
출력: HI의 경우 BTS T , HE의 경우도 BTS T
<br> 이유: "=" 이후로 ":=" 이없다면 아래 있는 매크로까지 전부 계산후 타겟안으로 들어간다.<br> 따라서 맨위에 전부쓰는것과 동일하다고 생각하자.

||||
|---|----|---|
|cat|파일 내용을 출력한다<br> 뒤에 "> txt파일" 을 붙이면 내용을 txt파일로 정장한다.| $cat /proc/cpuinfo<br> $cat /proc/cpuinfo>bts.txt|
|grep|파일을 찾는 명령어||
|find [ 경로 ] name "파일명"| - 파일을 찾는 명령어 ( ./ 는 폴더고 /는 디렉토리)<br> - **안의 이름이 포함되어있는 모든 파일 디렉토리 탐색<br>( *가 이름 앞이면 확장자 *가 뒤면 파일명 앞뒤 있으면 둘다)<br> - 파일혹은 디렉토리만 검색 (뒤에 -type f or d)를 붙임 |$find  ./dir -name "kfc.txt" <br> $find -name ```"*kfc*"```<br><br> $find -name "kfc.txt" -type f|
|history|모든 명령어 입력했던것들을 보여줌 ||
|du -sh ./디렉토리| 디렉토리 용량 확인 뒤에 안붙이면 현재 디렉토리 용량||
|$ls -alh ./a.log| 파일용량 확인은 이걸로인듯?|
|file [이름]|이름적은 것이 무슨type인지 확인|

<img src = "./Linux img/grep.JPG" width = 800>

||||
|---|----|---|
|tree| (설치해야함) 자신과 하위디렉토리들을 손쉽게 볼수있음|

> 산술 연산

||||
|---|----|---|
|$((내용))| 산술 연산으로 처리|```abc=$(($bts +123))```|

> 비교 연산