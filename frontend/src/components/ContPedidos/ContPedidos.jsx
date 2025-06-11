import React, { useState, useEffect } from 'react';
import axios from '../../axios'; // Ou a sua configuração do axios
import './ContPedidos.css';

function ContPedidos() {
    const [produtoInput, setProdutoInput] = useState('');
    const [descricaoProdutoInput, setDescricaoProdutoInput] = useState('');
    const [valorProdutoInput, setValorProdutoInput] = useState(''); 
    const [pagamentoSelecionado, setPagamentoSelecionado] = useState('Crédito');
    const [pedidos, setPedidos] = useState([]);
    const [observacoesDoPedido, setObservacoesDoPedido] = useState('');
    const [selectedClienteId, setSelectedClienteId] = useState(5);

    const fetchPedidosCliente = async () => {
        if (!selectedClienteId && selectedClienteId !== 0) {
            console.log("Nenhum cliente selecionado, não buscando pedidos.");
            return;
        }
        try {
            const response = await axios.get(`/pedidos/`);
            const data = response.data;
            if (data && Array.isArray(data.results)) {
                setPedidos(data.results);
            } else if (Array.isArray(data)) {
                setPedidos(data);
            } else {
                setPedidos([]);
            }
        } catch (error) {
            console.error("Erro ao buscar pedidos:", error.response ? error.response.data : error.message);
            setPedidos([]);
        }
    };

    useEffect(() => {
        fetchPedidosCliente();
    }, []);

    const handleSubmitNovoPedido = async (event) => {
        event.preventDefault();
        if (!produtoInput.trim() || !descricaoProdutoInput.trim()) {
            alert("Por favor, preencha o produto e a descrição.");
            return;
        }
        if (!valorProdutoInput || isNaN(parseFloat(valorProdutoInput)) || parseFloat(valorProdutoInput) <= 0) {
            alert("Por favor, informe um valor de pedido válido.");
            return;
        }

        const payloadObservacoes = observacoesDoPedido.trim() || 'N/A';

        const pedidoPayload = {
            cliente_id: selectedClienteId,
            produto: produtoInput.trim(),
            descricao: descricaoProdutoInput.trim(),
            valor_produto: parseFloat(valorProdutoInput).toFixed(2), // Adicionado
            observacoes: payloadObservacoes,
            forma_pagamento: pagamentoSelecionado,
        };

        try {
            const response = await axios.post('/pedidos/', pedidoPayload);
            alert("Pedido enviado com sucesso!");
            setProdutoInput(''); 
            setDescricaoProdutoInput('');
            setValorProdutoInput(''); // Limpar o campo de valor
            setObservacoesDoPedido('');
            setPagamentoSelecionado('Crédito');
            fetchPedidosCliente(); 
        } catch (error) {
            console.error("Erro ao criar novo pedido:", error.response ? error.response.data : error.message);
            alert("Falha ao criar pedido: " + (error.response?.data?.error || error.response?.data?.detail || error.message));
        }
    };

    return (
        <div className="pedidos-page">
            <section className="novo-pedido">
                <h3>Fazer Novo Pedido</h3>
                <p>Escolha o que deseja e envie seu pedido!</p>
                <form onSubmit={handleSubmitNovoPedido}>
                    <label htmlFor="produtoInput">Tipo do Produto:</label>
                    <input
                        id="produtoInput" type="text" placeholder="Digite o nome do produto"
                        value={produtoInput} onChange={(e) => setProdutoInput(e.target.value)} required
                    />

                    <label htmlFor="descricaoProduto">Descreva o seu produto:</label>
                    <input
                        id="descricaoProduto" type="text" placeholder="Estabelecimento, quantidade, etc."
                        value={descricaoProdutoInput} onChange={(e) => setDescricaoProdutoInput(e.target.value)} required 
                    />

                    {/* NOVO CAMPO DE VALOR */}
                    <label htmlFor="valorProduto">Valor do Pedido (R$):</label>
                    <input
                        id="valorProduto"
                        type="number"
                        placeholder="Ex: 50.00"
                        value={valorProdutoInput}
                        onChange={(e) => setValorProdutoInput(e.target.value)}
                        required
                        step="0.01"
                        min="0.01"
                    />

                    <label htmlFor="observacoes">Observações do Pedido:</label>
                    <input
                        id="observacoes" type="text" placeholder="Alguma observação? (opcional)"
                        value={observacoesDoPedido} onChange={(e) => setObservacoesDoPedido(e.target.value)}
                    />

                    <label htmlFor="pagamento">Forma de Pagamento:</label>
                    <select
                        id="pagamento" value={pagamentoSelecionado}
                        onChange={(e) => setPagamentoSelecionado(e.target.value)}
                    >
                        <option value="Crédito">Crédito</option>
                        <option value="Débito">Débito</option>
                        <option value="Pix">Pix</option>
                        <option value="Dinheiro">Dinheiro</option>
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
                                <strong>Pedido #{pedido.id}</strong> <br />
                                Produto: {pedido.produto} <br />
                                Descrição: {pedido.descricao} <br />
                                {pedido.observacoes && pedido.observacoes !== 'N/A' && (
                                    <>Observações: {pedido.observacoes}<br /></>
                                )}
                                Entregador: {pedido.entregador?.nome || 'Não atribuído'}<br />
                                
                                {/* --- SEÇÃO DE VALORES --- */}
                                {pedido.valor_total != null && (
                                  <>
                                    <hr style={{margin: '8px 0', border: '1px solid #eee'}}/>
                                    Valor do Produto: R$ {Number(pedido.valor_produto).toFixed(2).replace('.', ',')} <br />
                                    Taxa de Serviço: R$ {Number(pedido.taxa_servico).toFixed(2).replace('.', ',')} <br />
                                    <strong>Valor Total: R$ {Number(pedido.valor_total).toFixed(2).replace('.', ',')}</strong> <br />
                                    <hr style={{margin: '8px 0', border: '1px solid #eee'}}/>
                                  </>
                                )}
                                
                                <span>Data: {new Date(pedido.data_pedido).toLocaleString('pt-BR')}</span> <br />
                            </p>
                            
                            {/* Lógica dos botões de status */}
                            {pedido.status_atual === "Entregue" ? (
                                <button className="entregue" disabled>✓ Entregue</button>
                            ) : pedido.status_atual === "A caminho" ? (
                                <button className="acaminho" disabled>🕒 A caminho</button>
                            ) : pedido.status_atual === "Em Preparo" ? (
                                <button className="empreparo" disabled>🛠 Em preparo</button>
                            ) : pedido.status_atual === "Pago" ? (
                                <button className="pago" disabled>💲 Pago</button>
                            ) : (
                                <button className="pendente" disabled>⚪ {pedido.status_atual || 'Pendente'}</button>
                            )}
                        </div>
                    ))
                )}
            </section>
        </div>
    );
}

export default ContPedidos;