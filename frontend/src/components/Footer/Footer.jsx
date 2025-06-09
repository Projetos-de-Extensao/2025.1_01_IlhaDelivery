import React from "react";
import "./Footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <p className="footer-copy">&copy; {new Date().getFullYear()} Ilha Delivery</p>
        <div className="footer-links">
          <a href="#">Privacidade</a>
          <a href="#">Termos</a>
          <a href="#">Contato</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
