# 클릭 이벤트

## 1. 명령어
```html
 <button v-on:click = "bbq">눌러봐</button>
 ```
## 2. 예시
```html
  <body>
    <!-- HTML -->
    <div id="app">
      <h1>{{ message }}</h1>
      <button v-on:click="changeText">클릭</button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.min.js"></script>
    <script>
      // vue instance
      const app = new Vue({
        el: "#app",
        data: {
          message: "클릭을 눌러주세요.",
          nextMessage: "하하",
        },
        methods: {
          changeText() {
            this.message = this.nextMessage;
          },
        },
      });
    </script>
  </body>
  ```
- 버튼을 누르면 메세지가 변경되도록 설계
- 이때 button을 div안에 넣어야만 작동한다는 점에 주목 
<br>
->  이유: id="app"안에 들어있어야 const app으로 들어가기 때문
<br>
```html
    <!-- 이렇게 따로 빼서 실행 시킬수도 있기는 함(원리를 이해하기 위해서 분리해둔것이지
    같은 id면 div하나로 같이 묶자) -->
    <div id="app">
      <button v-on:click="changeText">클릭</button>
    </div>
```
