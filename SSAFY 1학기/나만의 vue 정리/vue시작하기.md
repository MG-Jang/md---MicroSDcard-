# Vue란 무엇일까
<br>
<br>

## 1. vue기본개념
- HTML, CSS, Java 등 웹페이지의 기능이 많아짐.
- 개발의 코드량이 많아지고 사용자 이벤트가 많아짐.
- 즉 DOM 제어 할 것이 많아지면 개발해야 할 js가 많아 짐. 
<br>
<br>

## 2 - 1. 기본 단축키
- ctrl + c : run serve 종료
- ctrl + s : 변경사항 저장(저장을 해야지만 변경사항이 적용됨!)
<br>
<br>

## 2 - 2. 터미널 명령어
- 실행 원하는 폴더 우측클릭 -> 터미널열기: 이렇게 하지 않으면 여러 파일이 있는경우 어떤 터미널이 열릴지 모른다.
- npm i : package.json에 있는 추가 모듈들을 자동으로 설치
- npm run serve : 서버를 실행(디폴트 값으로 로컬 8080을 실행, 만약 8080 이 실행중이면1씩 추가된 
주소로 실행)
<br>
  http://localhost:8080/
- npm run build: 배포용 빌드로 배포환경에서 사용할 파일들을 만들어 주는데 압축형태로 제공된다. (자세히는 잘 모르겠다.)
<br>
<br>

## 3. vue 인스턴스
- 뷰 인스턴스는 뷰로 화면을 개발 하기 위해 필수적으로 생성해야하는 기본 단위.
> 3가지의 방법 존재
``` html
<script>
    const app = new Vue({
        el: "# 선택자",
        // data 변수들이 들어가는 속성
        data: {
            message: "출력 부분",
        },
    })
</script>
```
인스턴스 안에 el(DOM element의 약자) 속성을 통해 뷰 인스턴스가 그려질 지점을 지정하고, data 속성에 화면에 보여질 데이터를 정의한 후
<br>
(data라는 프로퍼티는 vuejs에서 정해준 이름으로 다른 변수명로 사용 불가 또한 data 안에 들어 있는것은 객체)
```html
<div id="선택자">
    {{something}}
</div>
```
태그 이름과 출력할것을 안에 적어준다.
이때 중괄호 두개를 사용한 이유는 vue에서 data binding(데이터 묶기)를 위해 상용한다고 알아두자
<br>

ex)예시
```html
<body>
    <div id ="app">{{message}}</div>
    <!-- vue tag -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.min.js"></script>
    <script>
        const app = new Vue({
            el: "#app",
            data: {
                message: "출력부분",
            },
        })
    </script>
</body>
```
그렇다면 왜 {{message}}부분을 그냥 내가 원하는 출력으로 적어도 될텐데 왜 저렇게 불편하게 나누어 놨을까?
<br>

-> 왜냐면 이름을 변경하고 싶기 때문