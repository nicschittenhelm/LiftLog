import './styles/Main.scss'
import Navbar from "./components/Navbar.tsx" 
import DebugInput from './components/DebugInput.tsx'
import img1 from './assets/1.jpg'
import img4 from './assets/4.png'



function App() {
  return (
    <>
      <Navbar/>
      <div className='main-heading-wrapper'>
        <h1 className='main-heading'>
          <span>Log</span>
          <span>
            Your
          </span>
          <br></br>
          <span>Progress</span>
        </h1>
        <img className='main-heroimage' src={img4}></img>

        <div id='main-btn-wrapper'>
          <p>Button Here!</p>
        </div>
      </div>


      <div id='shape-wrapper'>
        <div id='main-shape'/>
      </div>


    </>
  )
}

export default App
