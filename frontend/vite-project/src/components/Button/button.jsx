import './Button.css'

export default function Button({children, onClick}) {
    // children is needed to pass parameters
    // <button>bla bla bla</button>
    // function handleClick() {
    //     console.log('button cl')
    // }




    return <button className='but' onClick={onClick} >{children}  </button>
}