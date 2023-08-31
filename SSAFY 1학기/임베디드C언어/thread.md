# tread 

## <span style="color:orange"> unistd.h </span>
- 의미: POSIX 운영체제 API에 대한 액세스를 제공하는 헤더파일. 
-  즉: 유닉스에서 사용하는 C컴파일러 라 생각하면 됨. window에서는 사용하지 않음.

## <span style="color:orange"> pthread.h </span>

- 의미: pthread란 POSIX Thread의 약자로 유닉스계열 POSIX시스템에서 병렬적으로 작동하는 소프트웨어를 작성하기 위하여 제공하는 API
-  즉: 스레드를 편하게 만들수 있게 도와주는 API

> 기본 명령어

pthread_create
-  pthread_create ( thread id, 쓰레드 속성, 함수, 파라미터)
-  Arg1 : thread id 저장될 변수 주소
-  Arg2 : 쓰레드 설정 (attribute) : NULL 은 Default 설정
-  Arg3 : 실행할 함수 이름
-  Arg4 : 함수에 인자 값을 전달해주고 싶을 때 사용

pthread_join
-  pthread_join (thread id, thread 리턴값)
1. pthread_create를 하면 커널 내부적으로, 쓰레드 제작 작업을 한다.
2. join을 만나면 쓰레드가 종료 됨을 기다린 후, 커널 내부 정리 작업을 한다.
-  pthread를 사용하면 pthread_join을 반드시 써주자.
-  만약 pthread_join을 하지 않으면
thread가 종료되어도 정리작업(메모리해제)를 하지 않는다.
- <span style="color:orange"> join은 &를 쓰지 않는다!!! </span>

> 기본 예시
```c
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void* abc()
{
    while (1) {
        printf("ABC\n");
        sleep(1);
    }

    return 0;
}

void* bts() {
    while (1) {
        printf("BTS\n");
        sleep(1);
    }

    return 0;
}

int main()
{
    pthread_t t1, t2;

    pthread_create(&t1, NULL, abc, NULL);
    pthread_create(&t2, NULL, bts, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    return 0;
}
```
gcc ./thread.c -o ./thread <span style="color:orange">-lpthread </span>
- 꼭 <span style="color:orange">-lpthread </span> 를 입력해야함!
- 실행결과: ABC BTS ABC BTS ....or
<br>ABC ABC BTS ABC....
- 죽 ABC BTS의 순서와 횟수는 무작위 이다. 이유는 아래서 설명 

> thread 인자값 넘기기

```C
#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void *abc(void *p)
{
    int *a = (int *)p;

    while (1) {
        printf("#%d\n", *a);
        sleep(1);
    }
}

int main() {
    int gv = 7;
    pthread_t tid;

    pthread_create(&tid, NULL, abc, &gv);
    pthread_join(tid, NULL);

    return 0;
}
```
결과:
```
#7
#7
#7
#7
...
```
- gv가 인자 값이 되어 p로 들어감

