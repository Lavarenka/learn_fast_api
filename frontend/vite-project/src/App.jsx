import {useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'


import './App.css'
import Header from "./components/Header.jsx";
import WayToTeach from "./components/WayToTeach.jsx";
import Button from "./components/Button/button.jsx";

import {differences} from "../data.js";

function App() {
    const [content, setContent] = useState(null)
    // useState  to change the state of a variable

    // let content = 'click button'
    function handleClick(type) {
        // console.log('butcl', type)
        setContent(type)
    }

    let tabContent = null

    if (content) {
        tabContent = <p>{differences[content]}</p>
    }else {
        tabContent = <p>Нажми н кнопку</p>
    }

    return (
        <div>
        <Header/>
            <main>
                <section>
                    <h3>
                        Наш подход к обучению
                    </h3>
                    <ul>
                        <WayToTeach/>
                        <WayToTeach/>

                    </ul>
                </section>
                <section>
                    <h3>Button</h3>
                    <Button onClick={() => handleClick('way')}>text</Button>
                    <Button onClick={() => handleClick('easy')}>text2</Button>
                    <Button onClick={() => handleClick('program')}>text3</Button>

                    {/*{content ? <p>{differences[content]}</p> : <p>Нажми н кнопку</p>}*/}
                    {/* Method 2  */}
                    {/*{!content && <p>Нажми н кнопку</p>}*/}
                    {/*{content && <p>{differences[content]}</p>}*/}
                    {tabContent}
                </section>
            </main>
        </div>


    )
}

export default App
