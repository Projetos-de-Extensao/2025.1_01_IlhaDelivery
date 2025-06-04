import React, { useState, useEffect } from 'react'; // 👈 Certifique-se de que useEffect está importado
import axios from '../../axios'; // Ou a sua configuração do axios
import './ContPedidos.css';

function ContPedidos() {
    // Seus estados existentes:
    const [tipoProdutoInput, setTipoProdutoInput] = useState('');
    const [descricaoProdutoInput, setDescricaoProdutoInput] = useState('');
    const [pagamentoSelecionado, setPagamentoSelecionado] = useState('Crédito');
    const [pedidos, setPedidos] = useState([]);
    const [selectedClienteId, setSelectedClienteId] = useState(4); // ID do cliente

    const fetchPedidosCliente = async () => {
        // Sua função fetchPedidosCliente (sem alterações aqui, ela já está boa)
        // A guarda if (!selectedClienteId && selectedClienteId !== 0) pode ser removida
        // se o backend sempre filtra pelo usuário do token e selectedClienteId não é usado na URL de GET.
        // Para este exemplo, vamos manter como está, assumindo que selectedClienteId = 4 é sempre válido.
        if (!selectedClienteId && selectedClienteId !== 0) {
            console.log("Nenhum cliente selecionado, não buscando pedidos.");
            return;
        }
        try {
            console.log("Buscando pedidos para o cliente ID:", selectedClienteId); // Adicionado log
            const response = await axios.get(`/pedidos/`);
            const data = response.data;
            console.log("Pedidos recebidos:", data); // Adicionado log

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

    // 👇 ADICIONE ESTE useEffect AQUI 👇
    useEffect(() => {
        console.log("Componente ContPedidos montado. Buscando pedidos iniciais...");
        fetchPedidosCliente(); // Chama a função para buscar os pedidos
    }, []); // O array de dependências vazio [] faz este efeito rodar UMA VEZ após a montagem.

    const handleSubmitNovoPedido = async (event) => {
        event.preventDefault();
        if (!tipoProdutoInput.trim()) {
            alert("Por favor, informe o tipo do produto.");
            return;
        }

        const descricaoCompleta = `Produto: ${tipoProdutoInput}. Detalhes Adicionais: ${descricaoProdutoInput || 'N/A'}`;
        const observacoesDoPedido = `Método de pagamento: ${pagamentoSelecionado}.`;

        const pedidoPayload = {
            cliente_id: selectedClienteId,
            descricao: descricaoCompleta,
            observacoes: observacoesDoPedido,
        };

        console.log("Payload que será enviado:", JSON.stringify(pedidoPayload, null, 2));

        try {
            const response = await axios.post('/pedidos/', pedidoPayload);
            console.log("Pedido criado:", response.data);
            alert("Pedido enviado com sucesso!");
            setTipoProdutoInput('');
            setDescricaoProdutoInput('');
            setPagamentoSelecionado('Crédito');
            fetchPedidosCliente(); // Rebusca os pedidos para atualizar a lista
        } catch (error) {
            console.error("Erro ao criar novo pedido:", error.response ? error.response.data : error.message);
            // A linha abaixo é onde você pega o HTML do erro 500
            const errorMessage = error.response?.data?.detail || JSON.stringify(error.response?.data) || error.message;
            // Se for uma string HTML longa (erro 500 do Django), podemos simplificar o alerta
            if (typeof errorMessage === 'string' && errorMessage.toLowerCase().includes('</html>')) {
                alert("Falha ao enviar pedido: Ocorreu um erro no servidor. Verifique o console do navegador e o terminal do Django para mais detalhes.");
            } else {
                alert("Falha ao enviar pedido: " + errorMessage);
            }
        }
    };

    const handleConfirmarPagamento = async (pedidoId) => {
        // Sua função handleConfirmarPagamento (sem alterações aqui)
        try {
            await axios.post(`/pedidos/${pedidoId}/confirmar_pagamento/`);
            alert('Pagamento do pedido confirmado!');
            fetchPedidosCliente();
        } catch (error) {
            console.error("Erro ao confirmar pagamento:", error.response ? error.response.data : error);
            alert("Falha ao confirmar pagamento: " + (error.response?.data?.error || error.message));
        }
    };

    // Seu JSX existente para o return:
    return (
        <div className="pedidos-page">
            <section className="novo-pedido">
                <h3>Fazer Novo Pedido</h3>
                <p>Escolha o que deseja e envie seu pedido!</p>
                <form onSubmit={handleSubmitNovoPedido}>
                    <label htmlFor="tipoProduto">Tipo do Produto:</label>
                    <input
                        id="tipoProduto"
                        type="text"
                        placeholder="Digite o nome do produto"
                        value={tipoProdutoInput}
                        onChange={(e) => setTipoProdutoInput(e.target.value)}
                        required
                    />

                    <label htmlFor="descricaoProduto">Descreva o seu produto:</label>
                    <input
                        id="descricaoProduto"
                        type="text"
                        placeholder="Estabelecimento, valor, quantidade, etc."
                        value={descricaoProdutoInput}
                        onChange={(e) => setDescricaoProdutoInput(e.target.value)}
                    />

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
                                Descrição: {pedido.descricao} <br />
                                <span>Data: {new Date(pedido.data_pedido).toLocaleString('pt-BR')}</span> <br />
                                {/* Outras informações que você queira exibir */}
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