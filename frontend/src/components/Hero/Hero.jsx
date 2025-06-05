import "./Hero.css";

function Hero() {
  return (
    <section className="hero-alt">
      <div className="hero-overlay">
        <div className="hero-box">
          <h1>Seu delivery local de confiança</h1>
          <p>Faça seu pedido!</p>

          <div className="hero-actions">
            <a href="/login" className="hero-btn secondary">Entrar na conta minha conta </a>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;
