from rest_framework import serializers
from .models import (
    Pedido, 
    Cliente, 
    Entregadores, 
    StatusPedido)

# ... (ClienteSerializer, EntregadoresSerializer, StatusPedidoSerializer) ...

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'user', 'nome', 'email', 'telefone', 'endereco', 'cpf']
        read_only_fields = ['id', 'user']

class EntregadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entregadores
        fields = ['id', 'nome', 'status', 'localizacao']
        read_only_fields = ['id']

class StatusPedidoSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = StatusPedido
        fields = ['id', 'pedido', 'status', 'status_display', 'data_status']
        read_only_fields = ['id', 'data_status']


class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), source='cliente', write_only=True, required=False
    )
    entregador = EntregadoresSerializer(read_only=True, allow_null=True)
    entregador_id = serializers.PrimaryKeyRelatedField(
        queryset=Entregadores.objects.all(), source='entregador', write_only=True, allow_null=True, required=False
    )
    status_historico = StatusPedidoSerializer(many=True, read_only=True, source='status_pedido')
    status_atual = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = [
            'id', 'cliente', 'cliente_id', 'entregador', 'entregador_id',
            'descricao', 'data_pedido', 'observacoes', 'pago',
            'status_historico', 'status_atual', 'forma_pagamento', 'produto',
            # --- CAMPOS ADICIONADOS ---
            'valor_produto', 'taxa_servico', 'valor_total'
        ]
        read_only_fields = [
            'id', 'data_pedido', 'pago', 'cliente',
            # --- CAMPOS CALCULADOS DEVEM SER APENAS LEITURA ---
            'taxa_servico', 'valor_total'
        ]

    def get_status_atual(self, obj):
        latest_status_obj = obj.status_pedido.order_by('-data_status').first()
        if latest_status_obj:
            return latest_status_obj.get_status_display()
        return "Pendente"