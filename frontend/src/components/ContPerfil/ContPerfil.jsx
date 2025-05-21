import React from "react";
import "./ContPerfil.css";

function ContPerfil() {
  return (
    <div className="perfil-page">
      <section className="perfil-box">
        <h3>Meu Perfil</h3>
        <p>Visualize e atualize suas informações pessoais.</p>
        <form>
          <div className="form-group">
            <label className="form-label">👤 Nome:</label>
            <input type="text" name="nome" placeholder="Seu Nome Completo" />
          </div>

          <div className="form-group">
            <label className="form-label">📍 Endereço:</label>
            <input type="text" name="endereco" placeholder="Rua Exemplo, 123 - Bairro" />
          </div>

          <div className="form-group">
            <label className="form-label">📞 Telefone:</label>
            <input type="text" name="telefone" placeholder="(xx) xxxxx-xxxx" />
          </div>

          <div className="form-group">
            <label className="form-label">📧 E-mail:</label>
            <input type="email" name="email" placeholder="seu@email.com" />
          </div>

          <button type="submit">Salvar Alterações</button>
        </form>
      </section>
    </div>
  );
}

export default ContPerfil;
