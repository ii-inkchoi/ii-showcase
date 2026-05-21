import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App  from './App'
import App2 from './App2'
import Landing from './Landing'
import Landing2 from './Landing2'
import './App.css'

const v = new URLSearchParams(window.location.search).get('v')

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    {v === 'app2' ? <App2 /> : v === 'app' ? <App /> : v === 'no-images' ? <Landing2 /> : <Landing />}
  </StrictMode>
)
