import React, { useState, useEffect } from 'react';
import axios from '../../axios'; // Ou a sua configuração do axios
import './ContPedidos.css';

function ContPedidos() {
    const [produtoInput, setProdutoInput] = useState(''); // Usado para "Tipo do Produto"
    const [descricaoProdutoInput, setDescricaoProdutoInput] = useState('');
    const [pagamentoSelecionado, setPagamentoSelecionado] = useState('Crédito');
    const [pedidos, setPedidos] = useState([]);
    const [observacoesDoPedido, setObservacoesDoPedido] = useState('');
    const [selectedClienteId, setSelectedClienteId] = useState(5); // ID do cliente

    const fetchPedidosCliente = async () => {
        if (!selectedClienteId && selectedClienteId !== 0) {
            console.log("Nenhum cliente selecionado, não buscando pedidos.");
            return;
        }
        try {
            console.log("Buscando pedidos para o cliente ID:", selectedClienteId);
            const response = await axios.get(`/pedidos/`);
            const data = response.data;
            console.log("Pedidos recebidos:", data);

            if (data && Array.isArray(data.results)) {
                setPedidos(data.results);
            } else if (Array.isArray(data)) {
                setPedidos(data);
            } else {
                console.warn("A resposta da API de pedidos não continha um array de pedidos esperado. Recebido:", data);
                setPedidos([]);
            }
        } catch (error) {
            console.error("Erro ao buscar pedidos:", error.response ? error.response.data : error.message);
            setPedidos([]);
        }
    };

    useEffect(() => {
        console.log("Componente ContPedidos montado. Buscando pedidos iniciais...");
        fetchPedidosCliente();
    }, []);

    const handleSubmitNovoPedido = async (event) => {
        event.preventDefault();
        if (!produtoInput.trim()) {
            alert("Por favor, informe o tipo do produto.");
            return;
        }
        if (!descricaoProdutoInput.trim()) { 
            alert("Por favor, descreva o seu produto.");
            return;
        }

        const payloadObservacoes = observacoesDoPedido.trim() || 'N/A';

        const pedidoPayload = {
            cliente_id: selectedClienteId,
            produto: produtoInput.trim(),
            descricao: descricaoProdutoInput.trim(),
            observacoes: payloadObservacoes,
            forma_pagamento: pagamentoSelecionado,
        };

        console.log("Payload que será enviado:", JSON.stringify(pedidoPayload, null, 2));

        try {
            const response = await axios.post('/pedidos/', pedidoPayload);
            console.log("Pedido criado:", response.data);
            alert("Pedido enviado com sucesso!");
            setProdutoInput(''); 
            setDescricaoProdutoInput('');
            setObservacoesDoPedido('');
            setPagamentoSelecionado('Crédito');
            fetchPedidosCliente(); 
        } catch (error) {
            console.error("Erro ao criar novo pedido:", error.response ? error.response.data : error.message);
            // A linha abaixo é a versão simplificada do tratamento de erro que você forneceu no último código.
            alert("Falha ao criar pedido: " + (error.response?.data?.error || error.response?.data?.detail || error.message));
        }
    };

    const handleConfirmarPagamento = async (pedidoId) => {
        try {
            await axios.post(`/pedidos/${pedidoId}/confirmar_pagamento/`);
            alert('Pagamento do pedido confirmado!');
            fetchPedidosCliente();
        } catch (error) {
            console.error("Erro ao confirmar pagamento:", error.response ? error.response.data : error);
            alert("Falha ao confirmar pagamento: " + (error.response?.data?.error || error.message));
        }
    };

    return (
        <div className="pedidos-page">
            <section className="novo-pedido">
                <h3>Fazer Novo Pedido</h3>
                <p>Escolha o que deseja e envie seu pedido!</p>
                <form onSubmit={handleSubmitNovoPedido}>
                    {/* Campo: Tipo do Produto */}
                    <label htmlFor="produtoInput">Tipo do Produto:</label>
                    <input
                        id="produtoInput"
                        type="text"
                        placeholder="Digite o nome do produto"
                        value={produtoInput}
                        onChange={(e) => setProdutoInput(e.target.value)}
                        required
                    />

                    {/* Campo: Descreva o seu produto */}
                    <label htmlFor="descricaoProduto">Descreva o seu produto:</label>
                    <input
                        id="descricaoProduto"
                        type="text"
                        placeholder="Estabelecimento, valor, quantidade, etc."
                        value={descricaoProdutoInput}
                        onChange={(e) => setDescricaoProdutoInput(e.target.value)}
                        required 
                    />

                    {/* Campo: Observações do Pedido */}
                    <label htmlFor="observacoes">Observações do Pedido:</label>
                    <input
                        id="observacoes"
                        type="text"
                        placeholder="Alguma observação para o pedido? (opcional)"
                        value={observacoesDoPedido}
                        onChange={(e) => setObservacoesDoPedido(e.target.value)}
                    />

                    {/* Campo: Pagamento */}
                    <label htmlFor="pagamento">Pagamento:</label>
                    <select
                        id="pagamento"
                        value={pagamentoSelecionado}
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
                                {/* Exibição ajustada de observações */}
                                {pedido.observacoes && pedido.observacoes !== 'N/A' && (
                                    <>Observações: {pedido.observacoes}<br /></>
                                )}
                                {/* 👇 LINHA ADICIONADA PARA EXIBIR O ENTREGADOR 👇 */}
                                {/* Ajuste 'pedido.entregador_nome' para o nome correto do campo em seus dados */}
                                <>Entregador: {pedido.entregador?.nome || 'Não atribuído'}<br /></>
                                
                                <span>Data: {new Date(pedido.data_pedido).toLocaleString('pt-BR')}</span> <br />
                            </p>
                            {/* Lógica dos botões de status (mantida como estava) */}
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