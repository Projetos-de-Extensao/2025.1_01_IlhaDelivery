import React, { useEffect, useState } from "react";
import "./ContPedidos.css";
import { getPedidos } from "../../services/api";

function ContPedidos() {
  const [pedidos, setPedidos] = useState([]);

  useEffect(() => {
    getPedidos()
      .then((response) => setPedidos(response.data))
      .catch((error) => console.error("Erro ao buscar pedidos:", error));
  }, []);

  return (
    <div className="pedidos-page">
      <section className="novo-pedido">
        <h3>Fazer Novo Pedido </h3>
        <p>Escolha o que deseja e envie seu pedido!</p>
        <form>
          <label>Tipo do Produto:</label>
          <input type="text" placeholder="Digite o nome do produto" />

          <label> Descreva o seu produto:</label>
          <input type="text" placeholder="Estabelecimento, valor, quantidade, etc." />

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

        {pedidos.length === 0 ? (
          <p>Nenhum pedido encontrado.</p>
        ) : (
          pedidos.map((pedido) => (
            <div className="pedido" key={pedido.id}>
              <p>
                <strong>Pedido #{pedido.id}</strong> Produto: {pedido.descricao}{" "}
                <span>Data: {pedido.data_pedido}</span>
              </p>
              <button className="pedido">
                {pedido.status === "Entregue"
                  ? <button className="entregue">✓ Entregue</button>
                  : pedido.status === "A caminho"
                  ? <button className="acaminho">🕒 A caminho</button>
                  : <button className="empreparo">🛠 Em preparo</button>}
              </button>
            </div>
          ))
        )}
      </section>
    </div>
  );
}

export default ContPedidos;
