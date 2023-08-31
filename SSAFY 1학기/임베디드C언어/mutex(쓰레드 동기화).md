# mutex

- 의미: 쓰레드가 한꺼번에 같은 레지스터에 접근하는 경우 racecondition이 발생한다.
- 이를 차단하기위해 프로세스 synchronization 알고리즘 중 mutex를 사용

> 사용법

- 헤더파일은 pthread에서 지원함으로 따로 pthread만 있으면 가능
-  pthread_mutex_init(&mutex, attr)
    -   mutex 객체 초기화
    -   attr 에 NULL을 넣으면 기본 값으로 처리
- pthread_mutex_destroy
  - 객체 제거
- pthread_mutex_lock
  - mutex lock을 요청하여 얻는다.
  - 얻을 수 있을 떄까지 block된다.
```C
#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

pthread_mutex_t mlock;  // 선언
pthread_t t[4];
int gv = 0;

void * abc() {
	pthread_mutex_lock(&mlock); // 객체 lock
	for (int i = 0; i < 1000; i++) gv++;
	pthread_mutex_unlock(&mlock); // lock 해제
}

int main() {

	// mutex 객체 초기화
	pthread_mutex_init(&mlock, NULL); 

	for (int i = 0; i < 4; i++) pthread_create(&t[i], NULL, abc, NULL);
	for (int i = 0; i < 4; i++) pthread_join(t[i], NULL);

	printf("%d\n", gv);
	return 0;
}

```