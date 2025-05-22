from rest_framework import viewsets
from .models import (
    Pedido,
    Cliente,
    Entregador,
    ItemPedido,
    StatusPedido,
)
from .serializers import (
    PedidoSerializer,
    ClienteSerializer,
    EntregadorSerializer,
    ItemPedidoSerializer,
    StatusPedidoSerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
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


class StatusPedidoViewSet(viewsets.ModelViewSet):
    queryset = StatusPedido.objects.all()
    serializer_class = StatusPedidoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
