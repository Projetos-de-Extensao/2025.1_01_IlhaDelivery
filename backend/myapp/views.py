from rest_framework import viewsets
from .models import Produto, Pedido, Avaliacao, Cliente
from .serializers import ProdutoSerializer, PedidoSerializer, AvaliacaoSerializer, ClienteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
        #serializer.save(creator=self.request.user)

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
        #serializer.save(creator=self.request.user)

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
        #serializer.save(creator=self.request.user)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
        #serializer.save(creator=self.request.user)