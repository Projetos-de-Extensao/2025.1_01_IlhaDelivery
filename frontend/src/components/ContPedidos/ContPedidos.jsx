import React from "react";
import "./ContPedidos.css";

function ContPedidos() {
  return (
    <div className="pedidos-page">

      <section className="novo-pedido">
        <h3>Fazer Novo Pedido </h3>
        <p>Escolha o que deseja e envie seu pedido!</p>
        <form>
          <label>Tipo do Produto:</label>
          <input type="text" placeholder="Digite o nome do produto" />

          
          <label> Descreva o seu produto:</label>
          <input type="text" placeholder="Estabelecimento, valor, quantidade, etc."/>


          <label>Pagamento:</label>
          <select>
            <option>Crédito</option>
            <option>Débito</option>
            <option>Pix</option>
            <option>Dinheiro</option>
          </select>

          <button type="submit">➤ Fazer Pedido</button>
        </form>
      </section>

      <section className="meus-pedidos">
        <h3>Meus Pedidos</h3>
        <p>Acompanhe seus pedidos em andamento e anteriores.</p>

        <div className="pedido">
          <p><strong>Pedido #1032</strong> Produto: Hambúrguer Artesanal <span>Data: 08/04/2025</span></p>
          <button className="entregue">✓ Entregue</button>
        </div>

        <div className="pedido">
          <p><strong>Pedido #1033</strong> Produto: Pizza Portuguesa <span>Data: 08/04/2025</span></p>
          <button className="acaminho">🕒 A caminho</button>
        </div>

        <div className="pedido">
          <p><strong>Pedido #1034</strong> Produto: Combo Sushi + Refri <span>Data: 08/04/2025</span></p>
          <button className="empreparo">🛠 Em preparo</button>
        </div>
      </section>
    </div>
  );
}

export default ContPedidos;
