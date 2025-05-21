import "./ContLogin.css";
import { Link } from "react-router-dom";

function ContLogin() {
  return (
    <div className="cont-login">
      <div className="login-box">
        <h1>Login</h1>
        <p>Acesse sua conta no Ilha Delivery</p>

        <form className="login-form">
          <input type="email" name="email" placeholder="E-mail" required />
          <input type="password" name="password" placeholder="Senha" required />
          <button type="submit">Entrar</button>
        </form>

        <div className="divider">ou</div>

        <p className="signup-link">
          Ainda não tem uma conta? <Link to="/cadastro">Cadastre-se</Link>
        </p>
      </div>
    </div>
  );
}

export default ContLogin;
