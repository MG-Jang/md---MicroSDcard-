- main 구문
```C
int main(int argc, char *argv[])
//여기서 argc는 서버 실행시 뒤에 port번호를
//붙이면 2 아니면 1의 값을 가진다. 
// 따라서 뒤에   if (argc != 2) 구문이 port번호를
// 붙이지 않으면 생성되는 이유다.

// argv는 실질적인 port 번호를 받는 배열 주소를 저장하는 변수 인듯?

```
- 문자
```C
write(clnt_sock, message, str_len);
// 문자를 입력 받고 클라이 언트에게 전송
// 여기서 message는 배열의 형태를 띄고
// 만약 메세지를 서버에서 출력하고 싶다면 (내가 추가한코드)
message[str_len] = 0;
printf("%s\n",message);
// 를 추가하면 서버상에서도 코드를 볼 수 있다.
```