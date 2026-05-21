import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App  from './App'
import App2 from './App2'
import Landing from './Landing'
import './App.css'

const v = new URLSearchParams(window.location.search).get('v')

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    {v === '2' ? <App2 /> : v === 'landing' ? <Landing /> : <App />}
  </StrictMode>
)
