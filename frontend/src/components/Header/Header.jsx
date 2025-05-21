import { Link } from "react-router-dom";
import { useState } from "react";
import './Header.css'

function Header() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="header">
  <div className="header-container">
    <h1 className="header-title">Ilha Delivery</h1>
    <button className="menu-button" onClick={() => setIsOpen(!isOpen)}>
      ☰
    </button>

    <nav className={`header-nav ${isOpen ? "open" : ""}`}>
      <ul>
        <li><Link to="/" className="nav-link" onClick={() => setIsOpen(false)}>Início</Link></li>
        <li><Link to="/pedidos" className="nav-link" onClick={() => setIsOpen(false)}>Pedidos</Link></li>
        <li><Link to="/sobre" className="nav-link" onClick={() => setIsOpen(false)}>Sobre</Link></li>
        <li><Link to="/perfil" className="nav-link" onClick={() => setIsOpen(false)}>Perfil</Link></li>
      </ul>
    </nav>
  </div>
</header>
  );
}

export default Header;
