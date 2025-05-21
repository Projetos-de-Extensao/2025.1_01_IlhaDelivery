from rest_framework.routers import DefaultRouter
from .views import (
    PedidoViewSet,
    ClienteViewSet,
    EntregadorViewSet,    
    ItemPedidoViewSet,
)

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'entregadores', EntregadorViewSet)
router.register(r'itens', ItemPedidoViewSet)



urlpatterns = router.urls