from django.contrib import admin
from .models import(
    Pedido,
    Cliente,    
    Entregadores,
    StatusPedido,

) 
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'entregador', 'descricao', 'observacoes', 'pago', 'data_pedido','produto', 'forma_pagamento')
    list_filter = ('pago', 'entregador', 'data_pedido')
    ordering = ('-data_pedido',)
    fieldsets = (
    ('Informações Básicas', {'fields': ('cliente', 'descricao', 'observacoes', 'pago',)}),
    ('Detalhes do Entregador', {'fields': ('entregador',)}),
    ('Produto e Pagamento', {'fields': ('produto', 'forma_pagamento',)}),
  )




admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Cliente)
admin.site.register(Entregadores)
admin.site.register(StatusPedido)






