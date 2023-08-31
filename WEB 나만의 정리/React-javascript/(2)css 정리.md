# CSS 정리

CSS(Cascading Style Sheets)의 약자로 사용자에게 문서를 표현하는 방법 또는 방식을 지정하는 언어. 즉 간단하게 페이지를 꾸미는(style) 역할이라 생각하면 됨.

js안에서도 style은 가능하다. 하지만 두번이상 사용하거나 다른 js에서 사용이 불가능하다.
즉 CSS로 객체화를 하는 것이 여러번 사용할 때는 더 효과적이다. 

## CSS 주요 style <hr>

|style|용도|참고사항|
|---|---|---|
|width|가로(px를 꼭 붙어여야함)|width: 100px|
|height|세로|height: 30px|
|color|글자 색상|color: aqua|
|color|글자 색상|color: aqua|
|margin|마진 영역의 크기|margin: 60px auto|

## CSS 작성 방법 <hr>

CSS는 크게 2가지 방식으로 작성이 가능하다. css내용은 동일하고 이름에 modules를 붙이거나 안 붙이거나. 그리고 붙이는 경우 js파일에서 불러오는 방식의 차이가 존재한다. 또한 component에서 작성하지 App에서 작성할지 2가지 방식의 차이도 존재. <br>
따라서 총 4가지의 방식이 존재 한다.

아래 예시는 CSS 확장자 차이에 대해 작성했다.
(파일명의 이름은 js와 왠만하면 동일하게 작성)

> 1. 파일명.css

Hello.css
```css 
.box {  
    width: 200px; 
    height: 50px; 
    background-color: green;
}
```
Hello.js
```html
import "./Hello.css";

<div className='box'>here box</div>
```

> 2. 파일명.modules.css


Hello.module.css
```css 
.box {  
    width: 200px; 
    height: 50; 
    background-color: green;
}
```
Hello.js
```html
import styles from "./Hello.module.css";

<div className={style.box}>here box</div>
```