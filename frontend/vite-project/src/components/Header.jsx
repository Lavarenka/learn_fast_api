import App from "../App.jsx";
import logo from '/vite.svg'
import {useState} from "react";


function Header() {
    const [now, setNow] = useState(new Date())

    setInterval(() => setNow(new Date()), 1000)

    return (
        <header>
            <h3>
                <img src={logo} alt=""/>
            </h3>
            <span>Время сейчас: { now.toLocaleTimeString()}</span>
        </header>
    )
}


export default Header