from rest_framework.routers import DefaultRouter
from .views import (
    ProdutoViewSet,
    PedidoViewSet,
    AvaliacaoViewSet,
    ClienteViewSet,
    EntregadorViewSet,    
    ItemPedidoViewSet,
    StatusEntregaViewSet,
)

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'entregadores', EntregadorViewSet)
router.register(r'itens', ItemPedidoViewSet)
router.register(r'status', StatusEntregaViewSet)  

urlpatterns = router.urls