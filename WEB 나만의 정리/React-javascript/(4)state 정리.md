# State

뭔가 객체를 생성하는 것 같은데 정확히는 아직 모르겠다.

```js
import {useState } from "react"; 

export default function Hello(){
    const [name, setName] = useState("Mike");

    return (
        <div id ="name">{name}</div>
    )
}
```