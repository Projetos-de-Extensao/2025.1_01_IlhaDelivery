from django.contrib import admin
from .models import(
    Pedido,
    Cliente,    
    Entregador,
    ItemPedido,
    StatusPedido,

) 
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'entregador', 'descricao', 'observacoes', 'pago', 'data_pedido')
    list_filter = ('pago', 'entregador', 'data_pedido')
    ordering = ('-data_pedido',)
    fieldsets = (
    ('Informações Básicas', {'fields': ('cliente', 'descricao', 'observacoes', 'pago',)}),
    ('Detalhes do Entregador', {'fields': ('entregador',)}),
  )




admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Cliente)
admin.site.register(Entregador)
admin.site.register(ItemPedido)
admin.site.register(StatusPedido)





