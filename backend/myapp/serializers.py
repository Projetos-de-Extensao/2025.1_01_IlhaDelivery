# myapp/serializers.py
from rest_framework import serializers
from myapp.models import(
    Pedido,
    Cliente,
    Entregador,
    ItemPedido,
    StatusPedido,
) 

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'entregador', 'data_pedido', 'observacoes', 'descricao', 'pago']
        read_only_fields = ['id', 'data_pedido']

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


class StatusPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusPedido
        fields = ['id', 'pedido', 'status']
        read_only_fields = ['id']