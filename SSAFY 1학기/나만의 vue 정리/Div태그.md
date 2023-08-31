# Div 태그

## 1. div 태그란 
div태그는 Division의 약자로 웹사이트의 레이아웃(전체적인 틀)을 만들때 주로 사용.

## 2. 사용법 및 예제
|태그 |속성|비고|
|------|---|---|
 ```<div>```|style|스타일|
 ```<div>```| width|가로크기|
 ```<div>```|height|세로크기|
 ```<div>```|border|테두리 굵기|
 ```<div>```|background-color|배경색상|
 ```<div>```|float|정렬|
 ```<div>```|margin|여백|
 ```html
1. style은 <div>태그의 스타일을 지정해주는 것으로 다른 속성들을 사용할 수 있게끔 해줍니다. <div style="">

2. width는 <div>의 가로 크기를 정해줍니다. px(픽셀)단위로도 정할 수 있고 %(비율)단위로도 정할 수 있습니다.

3. height는 <div>의 세로 크기를 정해줍니다. px(픽셀)단위로도 정할 수 있고 %(비율)단위로도 정할 수 있습니다.

4. border은 <div>의 테두리의 굵기를 정해줍니다. 숫자가 클수록 굵기가 굵어집니다.

5. background-color은 <div>태그의 배경색상을 정하는 속성입니다.

6. float은 div의 정렬(좌,우)을 하는 속성입니다. 가운데정렬은 안됩니다.

7. margin은 div의 정렬기준 끝에서부터 여백을 주는 속성입니다. (margin-top,margin,-bottom,margin-left,margi
```
<br>
<br>

# Script 요소
## 1. script 란
 태그는 자바스크립트와 같은 클라이언트 사이드 스크립트(client-side scripts)를 정의할 때 사용합니다.
 <br>
 script 요소는 스크립트 코드를 요소 내부에 직접 명시하거나, src 속성을 사용하여 외부 스크립트 파일을 참조할 수 있습니다. 하지만 src 속성이 명시된 script 요소에는 스크립트 코드를 직접 명시해서는 안 됩니다.
 <br>
