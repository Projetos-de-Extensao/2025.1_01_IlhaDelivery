from rest_framework.routers import DefaultRouter
from .views import (
    PedidoViewSet,
    ClienteViewSet,
    EntregadoresViewSet,    
    StatusPedidoViewSet,
)

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'entregadores', EntregadoresViewSet)
router.register(r'status', StatusPedidoViewSet)



urlpatterns = router.urls