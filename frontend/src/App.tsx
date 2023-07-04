import './styles/Main.scss'
import Navbar from "./components/Navbar.tsx" 
import DebugInput from './components/DebugInput.tsx'
import heroimg from './assets/liftlog_hero.png'



function App() {
  return (
    <>
      <Navbar/>
      <div className='main-heading-wrapper'>
        <h1 className='main-heading'>
          <span>Log</span>
          <span>Your</span><br></br>
          <span>Progress</span>
        </h1>
        <p>test</p>
      </div>

      <img className='main-heroimage' src={heroimg}></img>
      
      <div id='shape-wrapper'>
        <div id='main-shape'/>
      </div>


    </>
  )
}

export default App
