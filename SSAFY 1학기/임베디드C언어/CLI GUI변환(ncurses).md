# ncurses
- CLI로 GUI 같은 App을 만들고자 할 때 사용하는 library
- 설치: <span style="color:orange">sudo apt install libncursesw5-dev </span>
-  헤더파일 <span style="color:orange"> ncurses.h </span> 추가
-  gcc 컴파일시 <span style="color:orange"> >-lncursesw </span>을 넣어야함. 

> 기본형태

```C
#include<ncurses.h>

int main(){
    initscr();
    
    printw("hello");
    refresh()

    getch();
    endwin();

    return 0;
}
```

> ncurses 관련 함수

||||
|---|---|---|
|initscr()|ncurses 시작을 위한 내부 세팅|
|printw|printf대신 사용하자|
|getch() | 키를 눌러야 프로그램이 종료되도록 함|
|endwin()|ncurses 종료를 위한 내부 정리|
|refresh()|화면 갱신 명령어, <span style="color:orange">printw를 쓴뒤 꼭 써주자</span>|
|usleep(숫자)|us초(10^6) = 1초 를 나타냄 카운팅|(unistd.h 추가)|
|clear()|화면 전체를 삭제|
|move(y좌표,x좌표)|좌표를 움직임, row,col로 외워도됨|
|mvprintw(y,x,출력값)|move와 print가 합쳐진 형태|