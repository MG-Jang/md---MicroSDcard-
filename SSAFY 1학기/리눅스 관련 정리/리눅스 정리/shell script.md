# shell script 쉘 스크립트

>CLI Shell의 종류

- 우분투 기본 CLI Shell: Bash
- 현재 사용중인 쉘 확인:
  - cat /etc/passwd | grep bash
- CLI shell은 두가지 존재
    - dash : 데비안 암키스트 쉘, 경량 즉) 임베디드에서 많이 사용
    - bash 본 어게인 쉘, 기능 많고 무겁
    -  명령어는 둘이 거의 동일하다.
    -  dash 에서 bash 실행은 불가능, 반대는 가능

> shell script 개요

- if, for 변수들을 사용하여 프로그래밍 가능

- 상식:
    - 파이썬의 스크립트 실행기: pypy
    - 자바스크립트의 실행기: node.js

- 쉘 스크립트는 자동화 프로그램을 만들 때 쓴다. 확장자 .sh
  - 매번 초기 세팅해야 하는 반복 작업을 shell script로 자동화 시킴

> 스크립트 제작 및 실행

1. 확장자를 .sh로 파일 생성
2. 맨위에 #!/bin/bash 를 적어줌. (bash 대시 sh를 적으면 dash 쉘)
   - 쉬뱅이라고 부른다.
   -  이는 주석이 <span style = "color:orange">아니다. </span>
   - but  어떤 스크립트로 작동시켜줄지 알려주는 굉장히 중요한 문구 이다. 
3. 코드 작성후 (예시)
```
#!/bin/bash

echo HI
touch a.txt b.txt c.txt
ls -al ./*.txt
rm -r ./*.txt
echo BYE
```
4.  아래 명령어 입력
    - <span style = "color:orange">$ soruce [sh파일] </span>

- 만약 파이썬으로 작성하였다면
  - <span style = "color:orange">$ python3 파일이름.py</span>
- 주석은 #으로 입력

> 예시 코드

- 위에 <span style = "color:orange">#!/bin/bash</span>가 기본적으로 입력되어있다고 가정

<br>

1. <span style = "color:green">echo 로 파라미터 입력 받기 int main(..요부분..) 과 비슷한 느낌</span>

```bash
echo $1 
```
실행시 : source test.sh 100 이라 입력하면 100출력 숫자 대신 문자도 가능<br>
변수명을 무조건 1로 해야하는듯 그렇지 않으면 정상 작동 안함. 여러개의 파라미터 입력은 아래와 같다.


<br>

2. <span style = "color:green">soruce ./sum.sh 100 200 50 입력시 결과가 350이 나오게 만들어라</span>
 ```bash 
 echo $(( $1 + $2 + $3))
 ``` 

 3.  <span style = "color:green">입력받은 파라미터를 다른 변수명에 넣고 싶은경우
```bash
test=$1
echo result: $test
``` 

4. if문 만들기 (띄어쓰기 굉장히 ㅇ)
```bash
a = BTS
if [ $a = "BTS" ] ; then
  echo "BTS GOGO" 
else
  echo "NO!!"
fi
```

5. 실행후 변수 입력 받기
```bash
read n
echo result: $s
```

6. shell 명령어 입력(C에서는 system을 붙였지만 bash의 경우 그냥 아무것도 없이 쓰면됨)
```bash
date
```
7. 

> 사용시 에러 발생 요인

- bts = hahah 이유: 띄어쓰기가 존재하면 안됨