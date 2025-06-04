from rest_framework import viewsets
from .models import (
    Pedido,
    Cliente,
    Entregador,
    ItemPedido,
    StatusPedido,
    Produto,
)
from .serializers import (
    PedidoSerializer,
    ClienteSerializer,
    EntregadorSerializer,
    ItemPedidoSerializer,
    StatusPedidoSerializer,
    ProdutoSerializer,
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
    def get_queryset(self):
        queryset = StatusPedido.objects.all()

        status = self.request.query_params.get('status')
        if status in [choice[0] for choice in StatusPedido.STATUS_CHOICES]:
            queryset = queryset.filter(status=status)

        return queryset
    # permission_classes = [IsAuthenticatedOrReadOnly]
