import Welcome from "./Welcome";
import styles from "./Hello.module.css";  //module의 경우 style from을 사용


const Hello = function(){

    function showName() {
        console.log("JANG");
    }

    function showText(e){
        console.log(e.target.value)
    }

    return (
        <div>
            <p style={
{
    color : '#f00',
    borderRight : '2px solid #000',
    marginBottom : '30px' ,
    opacity: 0.5
}                
            }>Hello4</p>
            <Welcome/>
            <p>Hello2</p>
            <button onClick={showName}>show me</button>
            <button onClick={() =>{
                console.log("JANG2");
            }}>show me2 </button>
            <input type="text" onChange={showText}/>
            <div className={styles.box}>what</div>
        </div>
    )
}

export default Hello;