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
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'disponivel')
    list_filter = ('nome', 'preco', 'disponivel')  # ajuste 'categoria' para um campo existente em Produto

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido)
admin.site.register(Avaliacao)
admin.site.register(Cliente)
admin.site.register(Entregador)
admin.site.register(ItemPedido)  
admin.site.register(StatusEntrega)
admin.site.register(Carrinho)
admin.site.register(ItemCarrinho)




