# event 정리

tag안에 event를 설정하는 방식. ex)
```html
<tag event={함수 이름}><tag/>
```
많은 tag와 event들이 존재 하지만 대표적으로 사용되는 몇가지에 대해 작성.

> tag

|tag명|작동||
|---|---|---|
|button|버튼 생성|
|input|검색창 생성|

> event (event의 경우 이름이 on으로 거의 99프로 시작)

|envent|작동||
|---|---|---|
|onClick|누르기|
|onChange|변화 감지|


<br>

## 클릭 event <hr>

버튼을 누르는 경우 활성화.<br>
클릭이벤트를 생성하는 방법도 2가지가 존재

> 1. 함수를 따로 빼서 생성하는 방법 

Hello.js
``` html
function showName() {
    console.log("JANG");
}

<button onClick={showName}>show me</button>
```
- function은 클릭이벤트가 작동된 경우 실행

> 2. 함수를 따로 생성하지 않는 방법

Hello.js
```html
    <button onClick={() =>{
        console.log("JANG2");
    }}>show me2 </button>
```

- 작성 형식에 주의!!! ()=>{내용물}  , 지키지 않으면 error 발생


## 검색창 event <hr>

``` html
<input type="text" onChange={showText}/>
```