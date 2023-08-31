# 에어 마우스 제작

> 프로젝트 계획
- 목표
  - 자이로 센서를 사용하여 센서가 가르키는 방향으로 마우스가 이동하도록 설계
- 사용 모듈
  - stm32 board (디버깅 및 데이터 처리) 컴퓨터와는 URS
  - MPU 6050 (MEMS센서 온도,가속도, 자이로 , i2c 통신을 사용)

- 사용 언어 
  - stm workspace: STM 보드 디버깅 코드 작성
  - STM Studio: 데이터을 그래프(시각화)하여 보여줌
  - visual stdio: 데이터를 이용하여 마우스를 움직여줌 

> 실험과정

1. i2c통신을 이용하여 stm 보드와 MPU 가 통신 (SDA, SCL 두 채널이용)
2. stm 에서 이를 해석하여 문자열 형태로 해석 (STM studio 에서는 문자열 형태로 받지 않음, visual stdio에서 사용할 예정)
3. STM studio에 각각의 변수의 주소값을 import 받아 이를 bar graph 형태로 해석(현재 위치x,y,z, 가속 x,y,z, 온도 / 총 7개) 
4. visual stdio에서 받은 배열을 read함수를 이용하여 buf에 저장 
5. buf에 저장된 데이터는 \r, \n , " " 으로 데이터가 구별되어있다. 이를 잘라서 해석하기 위해 strtok함수를 사용(strtok에 대한 설명은 C알고리즘 참고)
6. a_x, a_y를 이용하여 마우스를 이동
7. SetCursorPos(1275, 700) 화면 중심에 마우스 포인터를 이동 

> sleep을 낮춘 경우(부드럽게 하기위해) 발생 문제점
- C main문에서 sleep을높게 하면 마우스가 끊어져서 움직임
- 이를 해결하기 위해 sleep을 낮추면 error가 발생 왜? <br>
-> stm보드에서 보내준 데이터 보다 C main에서 읽는 속도가 빠른경우 C main buf에 데이터가 들어오지 않아 오류가 발생

> 해결방안
- stm main 문에서 HAL_Delay 의 값을 sleep 보다 낮게 설정한다.  그러면 buf에 데이터가 갱신되는 속도가 높아져 error 발생x 
- 하지만 sleep이 50 이하로 내려 갈경우 HAL_Delay의 값을 10정도로 설정해야 error가 발생하지 않는다
  - 아마 주기가 빨라질수록 데이터 전송속도가 이를 따라가지 못하는 것으로 판단됨. 
- 따라서 50 에 10 정도가 한계로 판단됨.

> 배운점
- 센서의 민감도에 따라 어느정도를 사람의 움직임으로 판단할지, 조건문을 추가하여 사람의 미세한 움직임은 측정하지 않게 3000으로 설정
- sleep의 HZ를 낮추는 경우 발생할 수 있는 문제점 


> visual stdio mian 문 

```C
#define _crt_secure_no_warnings
#include "Serial.h"
#include <stdio.h>
#include <string.h>
#include<stdlib.h>
#include<windows.h>


int main()
{
	//SetCursorPos(1275, 700);// 내 환경 기준 화면 중간 값
	int moves = 10;
    Serial* serial = new Serial("COM7", 115200);
    if (!serial->isConnected()) return 0;
	int cnt = 0, x = 0, y = 0;
    char buf[300];
    while (1) {
		cnt++;
        int ret = serial->read(buf, 255);
        if (!ret) continue;

		int ax, ay, az;
		char *ptr = strtok(buf, "\r\n");
		printf("%d번 \n", cnt);
		ptr = strtok(NULL, "\r");
		ptr = strtok(NULL, " ");
		ax = atoi(ptr);
		//printf("%s\n", ptr);    // a_x
		printf("%d\n", ax);    // a_x
		ptr = strtok(NULL, " ");
		ay = atoi(ptr);
		//printf("%s\n", ptr);    // a_y
		printf("%d\n", ay);    // a_y

		ptr = strtok(NULL, " ");
		az = atoi(ptr);
		//printf("%d\n", ax);    // a_x
		printf("%d", az);    // a_z 

		// ax, ay 가 3000이상 값으로 데이터가 증가하면 센서를 움직인것으로 판단
		// y,x 값에 최대 최소 범위를 설정하여 화면밖으로 마우스가 나가는 것을 방지
		if (ax < -3000 && y < 700)  y += moves;   
		else if (ax > 3000 && y > -700) y -= moves;
		if (ay < -3000 && x > -1275)  x -= moves;
		else if (ay > 3000 && x < 1275) x += moves;


		printf("row: %d, col: %d",1275 + x, 700 + y);     
		SetCursorPos(1275 + x, 700 +y );
		//ptr = strtok(NULL, " ");
		//printf("%s\n", buf);
		Sleep(50);   // 작아질 수록 올 
		if (cnt == 400) break;
    }

    return 0;
}
```

stm 보드 main 문
```C
/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include <stdio.h>
#include "sd_hal_mpu6050.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
 I2C_HandleTypeDef hi2c1;

UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */
SD_MPU6050 mpu1;
SD_MPU6050_Result result;
/* USER CODE END PV */

float temper;
int16_t g_x, g_y, g_z;
int16_t a_x, a_y, a_z;

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_I2C1_Init(void);
static void MX_USART2_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
//uart2
int _write(int file, unsigned char* p, int len)
{
  HAL_UART_Transmit(&huart2, p, len, 20);
  return len;
}

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_I2C1_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */
  result = SD_MPU6050_Init(&hi2c1,&mpu1,SD_MPU6050_Device_0,SD_MPU6050_Accelerometer_2G,SD_MPU6050_Gyroscope_250s );
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */
      SD_MPU6050_ReadTemperature(&hi2c1,&mpu1);
      temper = mpu1.Temperature;

      SD_MPU6050_ReadGyroscope(&hi2c1,&mpu1);
      g_x = mpu1.Gyroscope_X;
      g_y = mpu1.Gyroscope_Y;
      g_z = mpu1.Gyroscope_Z;

      SD_MPU6050_ReadAccelerometer(&hi2c1,&mpu1);
      a_x = mpu1.Accelerometer_X;
      a_y = mpu1.Accelerometer_Y;
      a_z = mpu1.Accelerometer_Z;

      printf("%f\n\r", temper);
      printf("%d %d %d\n\r", g_x, g_y, g_z);
      printf("%d %d %d\n\r", a_x, a_y, a_z);

      HAL_Delay(10);
    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief I2C1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_I2C1_Init(void)
{

  /* USER CODE BEGIN I2C1_Init 0 */

  /* USER CODE END I2C1_Init 0 */

  /* USER CODE BEGIN I2C1_Init 1 */

  /* USER CODE END I2C1_Init 1 */
  hi2c1.Instance = I2C1;
  hi2c1.Init.ClockSpeed = 100000;
  hi2c1.Init.DutyCycle = I2C_DUTYCYCLE_2;
  hi2c1.Init.OwnAddress1 = 0;
  hi2c1.Init.AddressingMode = I2C_ADDRESSINGMODE_7BIT;
  hi2c1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
  hi2c1.Init.OwnAddress2 = 0;
  hi2c1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
  hi2c1.Init.NoStretchMode = I2C_NOSTRETCH_DISABLE;
  if (HAL_I2C_Init(&hi2c1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN I2C1_Init 2 */

  /* USER CODE END I2C1_Init 2 */

}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 115200;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

```