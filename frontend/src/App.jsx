import { useState } from 'react';
import './App.css';
import Inicio from './pages/Inicio';
import Sobre from './pages/Sobre';
import Login from './pages/Login';
import Pedidos from './pages/Pedidos';
import Perfil from './pages/Perfil';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Inicio />}/>
          <Route path="/sobre" element={<Sobre/>}/>
          <Route path="/login" element={<Login/>}/>
          <Route path="/pedidos" element={<Pedidos />}/>
          <Route path="/perfil" element={<Perfil />}/>
        </Routes>
      </Router>
    </>
  );
};

export default App
