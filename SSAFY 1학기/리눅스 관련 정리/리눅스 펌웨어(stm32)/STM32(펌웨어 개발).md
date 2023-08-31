# stm32 시작하기 

- 시작하는 법은 pdf 참고
	- 참고 사항
	- ioc에서 cpu 커넥트 부분을 변경하면 변경후 우측 상단에 있는 톱니바퀴모양을 눌러야 적용
	- main 문은 core -> src 로들어가면 있음.
	- 디버깅시 92프로까지 올라간후 error가 나면 stm32 뽑았다가 다시 연결 시도

## 1. MCU란 무언인가
- Mcrio Controller Unit의 약자
- 일반적으로 마이크로 컨트롤러라 불림
- 프로그램을 통해 제어나 연산이 가능
- TV, 냉장고, 세탁기 등에 들어감

## 2. STM32란
- MCU의 한 제품으로 가장 현재 선호되는 제품
- MUC의 한예로 라즈베리 파이도 있다. 하지만 현업에서 사용되는 것은 STM Chipset이 들어감
- 주의! STM32란 칩셋과 메인보드가 결합된 형태이다. 즉 칩셋MCU의 명칭이 아니다.
- STM32에는 트레이서를 위한 디버거가 내장되어있음.
- 내가 사용한 STM32 MCU의 칩셋의 정확한 명칭은 "STM32F103RB" 이다.
- STM32에는 디버깅과 각종 부품이 포함된 메인보드 + STM32F103RB칩
- 따라서 실제 사용될때는 STM32F103RB을 사용하기에 STM32cubeIDE를 사용할때 board selector에서 고르기 보단 MCU chip에서 고르는 것이 더 공부에 도움이된다.
  - 메인 보드를 고르면 칩과 연결된 부분들이 이미 많이 setting이 되어있다.
- 외장 오실레이터 탑재는 "안된" 제품을 사용(오실레이터란 일정한 주기로 clock을 만들어주는 제품)

## 3. 사용 프로그램(STM CubeIDE)
- STM CubeIDE를 이용하여 프로그램을 짠다. ARM GCC 기반 무료 IDE
- 임베디드 보드의 초기세팅(Startup.s 코드 작성 / Clock 설정 / 레지스터 설정) 등이 어렵기 때문에 대신해주는 역할
  
## 4.mobaxterm 연결

> 2가지 방식이 존재
- USART : Sync통신
	- Clock PIN 을 하나 더 사용하여 ,Clock 을 기준으로 Sync( 박자 를 맞춘다
	- PIN 3 개 사용 (TX, RX, CK)
- UART : Async통신
	- Clock PIN 없이 , Start / End bit 를 추가적으로 사용하여 통신
	- PIN 2 개 사용 (TX, RX)
```C
	  HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, 1);
	  HAL_Delay(100);
	  HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, 0);
	  HAL_Delay(100);
```