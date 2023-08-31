// import logo from './logo.svg';
import './App.css';
import Hello from './component/Hello';
import Welcome from './component/Welcome';

function App() {
  // const각각이 객체, const로 선언 후 사용하지 않으면 error 발생!
  const name = "Jang"; // 객체 생성 방식1
  const naver = {  // 객체 생성 방식2
    name: "네이버",
    url: "https://naver.com",
  };
  return (  // App이라는 클래스 생성
    <div className="App">   
      <Hello/>
      <Welcome/>
      <h1>{name}</h1>
      <h1>{naver.name}</h1>
    </div>
  );
}

export default App;
