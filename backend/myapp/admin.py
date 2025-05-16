from django.contrib import admin
from .models import(
    Produto,
    Pedido,
    Avaliacao,
    Cliente,    
    Entregador,
    ItemPedido,
    StatusEntrega,
    Carrinho,
    ItemCarrinho
) 


admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Avaliacao)
admin.site.register(Cliente)
admin.site.register(Entregador)
admin.site.register(ItemPedido)  
admin.site.register(StatusEntrega)
admin.site.register(Carrinho)
admin.site.register(ItemCarrinho)




