from rest_framework import viewsets
from .models import (
    Pedido,
    Cliente,
    Entregador,
    StatusPedido,
)
from .serializers import (
    PedidoSerializer,
    ClienteSerializer,
    EntregadorSerializer,
    StatusPedidoSerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import serializers



class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    # permission_classes = [IsAuthenticated] # Já definido globalmente

    def get_queryset(self):
        user = self.request.user # Usuário do token
        if user.is_authenticated:
            try:
                # Encontra o Cliente associado ao User logado.
                # Ajuste 'user.cliente' se o related_name for diferente ou se você não tem um OneToOneField direto.
                # A forma Cliente.objects.filter(user=user).first() é mais segura.
                cliente_logado = Cliente.objects.filter(user=user).first()
                if cliente_logado:
                    # Retorna apenas os pedidos DESTE cliente
                    return Pedido.objects.filter(cliente=cliente_logado).order_by('-data_pedido')
                elif user.is_staff: # Opcional: admin vê tudo
                    return Pedido.objects.all().order_by('-data_pedido')
                return Pedido.objects.none() # Usuário autenticado, mas sem perfil de cliente
            except AttributeError: # Caso User não tenha o atributo reverso para Cliente
                return Pedido.objects.none()
        return Pedido.objects.none()

    def perform_create(self, serializer):
        user = self.request.user # Usuário do token
        if user.is_authenticated:
            try:
                cliente_logado = Cliente.objects.filter(user=user).first()
                if cliente_logado:
                    # Salva o pedido, associando-o automaticamente ao cliente_logado.
                    # Isso garante que o cliente_id enviado pelo frontend (se houver)
                    # seja ignorado em favor do cliente do usuário autenticado,
                    # o que é mais seguro e consistente para um "fake login".
                    serializer.save(cliente=cliente_logado)
                else:
                    raise serializers.ValidationError(
                        "Nenhum perfil de cliente encontrado para o usuário autenticado."
                    )
            except AttributeError:
                 raise serializers.ValidationError(
                    "Erro ao encontrar perfil de cliente para o usuário autenticado."
                )
        else:
            # Isso não deve acontecer devido à permissão IsAuthenticated
            raise serializers.ValidationError("Usuário não autenticado.")


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class EntregadorViewSet(viewsets.ModelViewSet):
    queryset = Entregador.objects.all()
    serializer_class = EntregadorSerializer
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
