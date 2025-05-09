from rest_framework import viewsets
from .models import (
    Produto,
    Pedido,
    Avaliacao,
    Cliente,    
    Entregador,
    ItemPedido,
    StatusEntrega,
)
from .serializers import (
    ProdutoSerializer,
    PedidoSerializer,
    AvaliacaoSerializer,
    ClienteSerializer,
    EntregadorSerializer,
    ItemPedidoSerializer,
    StatusEntregaSerializer,
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