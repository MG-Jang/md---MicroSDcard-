# low level 파일입출력

> 파일 오픈하기
-  open: 파일 열기
-  read: 파일 읽기
-  close 파일 닫기

> open system 구성
- fp에 오픈된 path의 내용을 저장
```C
int fp = open(path,flag,mode);
```
> open system flag
- 필수 옵션 선택(3개중 하나 선택)
  - O_RDONLY : 읽기 전용
  - O_WRONLY : 쓰기 전용
  - O_RDWR : 읽기 쓰기 모두 가능<br>(둘다 가능 이것만 사용해도 무방함)
- 추가옵션(or 연산 사용)
    - O_CREAT : 없으면 새로 생성
    - O_APPEND : 덧붙이기
    - O_TRUNC : 파일 내용 제거 후 사용

> open system mode
- write의 경우 파일 권한, 0xxx 값을 넣으면 된다.
    -   0777: rwxrwxrwx
    -   0644: rw-r--r--

> read system 구성
```
read(fp)
```

> 사용 예시
- test.txt 작성 (아무 내용이나 상관x)
- test.c 작성
```C
  #include <stdio.h>
  #include <sys/types.h>
  #include <sys/stat.h>
  #include <fcntl.h>
  #include <unistd.h>
   
  int main() {
        //open, test.txt파일을 , 읽기 전용으로 , 읽기 전용이므로 write설정은 필요 x이므로 0
      int fd = open("./test.txt",O_RDONLY,0);   
       // 내용을 담을 buf 생성
      char buf[1000]={0}; 
      //read에서 999개의 문자를 저장 -1을 뺀이유는 \n을 저장하기 위할 것으로 추정
      read(fd,buf,1000-1); 
      // 문자 출력
      printf("%s",buf);  
      // 문서닫기
      close(fd);  
      return 0;
 }

```
