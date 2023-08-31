# ssd project

> 1. 개요
```
ssd는 최소 저장 공간이 4kb이다.
즉 'A' 하나만 존재해도 4kb
'AB' 두개 존재해도 4kb를 차지한다.
```

> 2. 구현

- read, write를 구현 할 예정
그리고 LBA(Logical Block Address) 단위는 실제로는 4kb이지만 이번 프로젝트는 4byte를 사용

> 명령어 예시

- write 3 0xAAAABBBB
    - 3 번 LBA 에 0xAAAABBB 를 기록한다
    - ssd 에 명령어를 전달한다
- read 3
  - 3 번 LBA 를 읽는다.
  - ssd 에 명령어를 전달한다
  - result.txt 에 적힌 결과를 화면에 출력한다

> 설계

1. 16진수로 입력 받은 문자를 계산하기 쉽게 하기위해
  10진수를 2진수로 변경해주는 bin함수 제작

```C
void bin(int tmp) {    // 10진수 2진수로 바꿔 표현
	int binarry = 0 , expo = 0;
	while(1) {
		int k = pow(2, expo);
		if (tmp / k == 0) break;
		expo++;
	}
	expo--;
	while (1) {
		if (tmp - pow(2, expo) >= 0) {
			binarry += pow(10, expo);
			tmp = tmp - pow(2, expo);
		}
		if (expo == 0)break;
		expo--;
	}
	printf("%d\n", binarry);
}

int main(){
	char a[10] = "0x0A";
	int num;
	num = strtol(a, NULL, 16); // 16진수를 10진수로 변경
  bin(num);
  return 0 ;
}
```