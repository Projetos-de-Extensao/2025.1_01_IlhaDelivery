import { useEffect, useState } from "react";
import instaIcon from "../../assets/insta.png";
import "./Footer.css";

function Footer() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.innerHeight + window.scrollY;
      const pageHeight = document.documentElement.scrollHeight;
      setIsVisible(scrollPosition >= pageHeight - 10);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <footer className={`footer ${isVisible ? "visible" : ""}`}>
      <div className="footer-container">
        <div>
          <img src={instaIcon} alt="icone do instagram" className="footer-icons" />
        </div>
      </div>
    </footer>
  );
}

export default Footer;