import './styles/Main.scss'
import Navbar from "./components/Navbar.tsx" 
import DebugInput from './components/DebugInput.tsx'
import heroimg from './assets/liftlog_hero.png'



function App() {
  return (
    <>
      <Navbar/>
      <div className='main-heading-wrapper'>
        <h1 className='main-heading'>Keep progressing by <span>logging</span> your workouts with us!</h1>
        <p>test</p>
      </div>
      <img className='main-heroimage' src={heroimg}></img>

    </>
  )
}

export default App
