import React, { useEffect, useState } from "react";
import "./ContPedidos.css";

const apiUrl = "http://127.0.0.1:8000/api/contents/";

// Função para obter e listar conteúdos
async function fetchPedidos() {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    const contentTable = document.querySelector("#pedidosTable tbody");
    contentTable.innerHTML = "";

    data.forEach((pedido) => {
      const row = `
                        <tr>
                            <td>${pedidos.id}</td>
                            <td>${pedidos.cliente}</td>
                            <td>${pedidos.entregador}</td>
                            <td>${pedidos.data_pedido}</td>
                        </tr>
                    `;
      contentTable.innerHTML += row;
    });
  } catch (error) {
    console.error("Erro ao buscar conteúdos:", error);
  }
}

// Função para adicionar novo conteúdo
async function addPedido(event) {
  event.preventDefault();

  const titleElement = document.getElementById("title");
  const descriptionElement = document.getElementById("description");
  const fileUrlElement = document.getElementById("file_url");
  const thumbnailUrlElement = document.getElementById("thumbnail_url");
  const contentTypeElement = document.getElementById("content_type");
  const isPublicElement = document.getElementById("is_public");
  const creatorElement = document.getElementById("creator");

  if (!titleElement || !descriptionElement || !fileUrlElement || !thumbnailUrlElement || !contentTypeElement || !isPublicElement || !creatorElement) {
    alert("Erro: Um ou mais elementos do formulário não foram encontrados.");
    return;
  }

  const title = titleElement.value;
  const description = descriptionElement.value;
  const file_url = fileUrlElement.value;
  const thumbnail_url = thumbnailUrlElement.value;
  const content_type = contentTypeElement.value;
  const is_public = isPublicElement.checked;
  const creator = creatorElement.value;

  const contentData = {
    title,
    description,
    file_url,
    thumbnail_url,
    content_type,
    is_public,
    creator
  };

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(contentData),
    });

    if (response.ok) {
      alert("Conteúdo adicionado com sucesso!");
      fetchContents(); // Atualiza a lista de conteúdos
      document.getElementById("contentForm").reset(); // Limpa o formulário
    } else {
      const errorData = await response.json();
      alert(`Erro ao adicionar conteúdo 1: ${errorData.message || response.statusText}`);
    }
  } catch (error) {
    console.error("Erro ao adicionar conteúdo 2:", error);
  }
}

// Inicializar a página carregando os conteúdos
document.addEventListener("DOMContentLoaded", fetchContents);

// Evento de envio do formulário
document.getElementById("contentForm").addEventListener("submit", addContent);
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
                <strong>Pedido #{pedido.id}</strong> Produto: {pedido.produto || "N/A"}{" "}
                <span>Data: {pedido.data_pedido ? new Date(pedido.data_pedido).toLocaleDateString() : "N/A"}</span>
              </p>
              {renderStatusButton(pedido.status)}
            </div>
          ))
        )}
      </section>
    </div>
  );
}

export default ContPedidos;