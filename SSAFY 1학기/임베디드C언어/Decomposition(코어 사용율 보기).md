# decomposition

## data decomposition

- 데이터 단위로 분해하여 thread programming 
- 코어의 최고 효율을 낼 수 있다.

> decomposition사용시 주의 할 요소들

## Race Condition (경쟁상태)

- 두개 이상의 프로세스 or 쓰레드가 하나의 자원에 접근 하기 위해 경생하는 상태 


## Critical Section (임계영역)

- Thread / Process가 동시에 접근해서 안되는 곳
- HW 장치를 사용하는 곳 / Shared Resource (전역 변수 등)

> 위와 같은 문제를 해결하기 위한 방법

## Thread / Process Synchronization

- Critical Section을 동시에 수행하지 않도록 않게 하기 위해
Thread 간 협의를 맞추는 것

- 둘이서 하나의 HW 자원을 쓰거나 / 하나의 변수를 사용할 때,
한명씩 돌아가면서 쓰기 위해 협의를 봐야 함

- 동기화 알고리즘은 pthreads가 지원
  -  mutex 사용 예정 

> htop
- 리눅스 프로세스를 보는 명령어(top) 보다 더 간편하게 보는 유틸리티.
- 프로세스 사용률을 확인 할 수 있음.
- 설치: sudo apt install htop –y
- 실행: htop
