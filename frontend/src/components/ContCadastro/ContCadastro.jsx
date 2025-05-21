import "./ContCadastro.css";
import { Link } from "react-router-dom";

function ContCadastro() {
  return (
    <div className="cont-cadastro">
      <div className="cadastro-box">
        <div className="cadastro-welcome">
          <h1>Bem-vindo ao Ilha Delivery</h1>
          <p>Cadastre-se para começar a usar o melhor serviço de entrega da Ilha Primeira.</p>
        </div>

        <div className="cadastro-form">
          <h2>Criar Conta</h2>
          <form>
            <input type="text" name="name" placeholder="Nome completo" required />
            <input type="email" name="email" placeholder="E-mail" required />
            <input type="tel" name="phone" placeholder="Número de telefone" required />
            <input type="password" name="password" placeholder="Senha" required />
            <input type="password" name="confirmPassword" placeholder="Confirme sua senha" required />
            <button type="submit" className="submit-btn">Cadastrar</button>
          </form>

          <div className="divider">ou</div>

          <p className="login-text">
            Já possui uma conta? <Link to="/login">Faça login</Link>
          </p>
        </div>
      </div>
    </div>
  );
}

export default ContCadastro;
