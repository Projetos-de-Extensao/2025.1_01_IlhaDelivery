from rest_framework.routers import DefaultRouter
from .views import (
    ProdutoViewSet,
    PedidoViewSet,
    AvaliacaoViewSet,
    ClienteViewSet,
    EntregadorViewSet,    
    ItemPedidoViewSet,
    StatusEntregaViewSet,
    CarrinhoViewSet,
    ItemCarrinhoViewSet
)

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'entregadores', EntregadorViewSet)
router.register(r'itens', ItemPedidoViewSet)
router.register(r'status', StatusEntregaViewSet)
router.register(r'carrinhos', CarrinhoViewSet)
router.register(r'itens_carrinho', ItemCarrinhoViewSet)


urlpatterns = router.urls