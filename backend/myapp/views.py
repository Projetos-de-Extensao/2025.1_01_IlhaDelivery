from rest_framework import viewsets
from .models import (
    Produto, Pedido, Avaliacao, Cliente,    
    Entregador, ItemPedido, StatusEntrega,
    Carrinho, ItemCarrinho
)
from .serializers import (
    ProdutoSerializer,
    PedidoSerializer,
    AvaliacaoSerializer,
    ClienteSerializer,
    EntregadorSerializer,
    ItemPedidoSerializer,
    StatusEntregaSerializer,
    CarrinhoSerializer,
    ItemCarrinhoSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class EntregadorViewSet(viewsets.ModelViewSet):
    queryset = Entregador.objects.all()
    serializer_class = EntregadorSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class StatusEntregaViewSet(viewsets.ModelViewSet):
    queryset = StatusEntrega.objects.all()
    serializer_class = StatusEntregaSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ItemCarrinhoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]