# myapp/serializers.py
from rest_framework import serializers
from myapp.models import(
    Produto, Pedido, Avaliacao, Cliente,
    Entregador, ItemPedido, StatusEntrega, 
    Carrinho, ItemCarrinho
) 
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'descricao', 'disponivel']
        read_only_fields = ['id']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'entregador', 'data_pedido', 'observacoes']
        read_only_fields = ['id', 'data_pedido']

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'produto', 'cliente', 'nota', 'comentario']
        read_only_fields = ['id']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'endereco', 'cpf']
        read_only_fields = ['id']

class EntregadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entregador
        fields = ['id', 'nome', 'status', 'localizacao']
        read_only_fields = ['id']

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['id', 'pedido', 'produto', 'quantidade']
        read_only_fields = ['id']

class StatusEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusEntrega
        fields = ['id', 'pedido', 'status', 'horario']
        read_only_fields = ['id', 'horario']

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ['id', 'cliente']
        read_only_fields = ['id']

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrinho
        fields = ['id', 'carrinho', 'produto', 'quantidade']
        read_only_fields = ['id']