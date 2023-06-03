import './styles/Main.scss'
import Navbar from "./components/Navbar.tsx" 
import DebugInput from './components/DebugInput.tsx'

function App() {
  return (
    <>
      <Navbar/>
      <h1>Hello World</h1>
      <p>LiftLog Website</p>

      <DebugInput/>
    </>
  )
}

export default App
