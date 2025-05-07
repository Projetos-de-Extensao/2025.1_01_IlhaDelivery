# myapp/serializers.py
from rest_framework import serializers
from myapp.models import Produto
from myapp.models import Pedido
from myapp.models import Avaliacao
from myapp.models import Cliente
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'descricao', 'disponivel']
        read_only_fields = ['id']


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'produto', 'quantidade', 'data_pedido']
        read_only_fields = ['id', 'data_pedido']


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'produto', 'usuario', 'nota', 'comentario']
        read_only_fields = ['id']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'endereco', 'cpf']
        read_only_fields = ['id']