import { motion } from "framer-motion";
import "./SobreInfo.css";

function SobreInfo() {
  return (
    <div className="about-container">
      <motion.h1
        className="about-title"
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
      >
        Sobre Nós
      </motion.h1>

      {/* Descrição animada */}
      <motion.p
        className="about-text"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, ease: "easeOut", delay: 0.3 }}
      >
        Bem-vindo ao <span className="highlight">Ilha Delivery</span>! Nossa missão é conectar você aos melhores serviços e produtos da região, garantindo rapidez, qualidade e praticidade.
      </motion.p>

      {/* Cards de Informações */}
      <div className="about-cards">
        <motion.div
          className="about-card"
          whileHover={{ scale: 1.05 }}
        >
          <h3>🚀 Missão</h3>
          <p>Entregar qualidade e agilidade a cada cliente.</p>
        </motion.div>

        <motion.div
          className="about-card"
          whileHover={{ scale: 1.05 }}
        >
          <h3>🌍 Visão</h3>
          <p>Ser a plataforma referência em delivery na ilha.</p>
        </motion.div>

        <motion.div
          className="about-card"
          whileHover={{ scale: 1.05 }}
        >
          <h3>💡 Valores</h3>
          <p>Compromisso, inovação e excelência.</p>
        </motion.div>
      </div>
    </div>
  );
};

export default SobreInfo;
