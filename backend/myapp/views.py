from rest_framework import viewsets
from .models import (
    Pedido,
    Cliente,
    Entregadores,
    StatusPedido,
)
from .serializers import (
    PedidoSerializer,
    ClienteSerializer,
    EntregadoresSerializer,
    StatusPedidoSerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    # permission_classes = [IsAuthenticated] # Já definido globalmente

    def get_queryset(self):
        user = self.request.user # Usuário do token
        if user.is_authenticated:
            try:
                cliente_logado = Cliente.objects.filter(user=user).first()
                if cliente_logado:
                    return Pedido.objects.filter(cliente=cliente_logado).order_by('-data_pedido')
                elif user.is_staff: 
                    return Pedido.objects.all().order_by('-data_pedido')
                return Pedido.objects.none() 
            except AttributeError: 
                return Pedido.objects.none()
        return Pedido.objects.none()

    def perform_create(self, serializer):
        user = self.request.user # Usuário do token
        if user.is_authenticated:
            try:
                cliente_logado = Cliente.objects.filter(user=user).first()
                if cliente_logado:
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
            raise serializers.ValidationError("Usuário não autenticado.")


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [IsAuthenticated] # Assumindo global

    @action(detail=False, methods=['get', 'put', 'patch'], url_path='me', permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        try:
            # Busca o cliente associado ao usuário logado
            cliente = Cliente.objects.filter(user=user).first()
            if not cliente:
                return Response(
                    {"detail": "Perfil de cliente não encontrado para este usuário."},
                    status=status.HTTP_404_NOT_FOUND
                )

            if request.method == 'GET':
                serializer = self.get_serializer(cliente)
                return Response(serializer.data)

            # Para PUT (atualização completa) ou PATCH (atualização parcial)
            elif request.method in ['PUT', 'PATCH']:
                # Para PATCH, usamos partial=True para permitir atualizações parciais
                # Para PUT, partial seria False por padrão (espera todos os campos obrigatórios)
                # Usar partial=True para PUT também o torna mais flexível como um PATCH.
                serializer = self.get_serializer(cliente, data=request.data, partial=True) 
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except AttributeError:
            return Response(
                {"detail": "Erro ao tentar acessar informações do usuário."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"detail": f"Ocorreu um erro interno: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class EntregadoresViewSet(viewsets.ModelViewSet):
    queryset = Entregadores.objects.all()
    serializer_class = EntregadoresSerializer
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
