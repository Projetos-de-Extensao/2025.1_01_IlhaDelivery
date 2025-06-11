from django.contrib import admin
from .models import(
    Pedido,
    Cliente,    
    Entregadores,
    StatusPedido,

) 
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'entregador', 'produto', 'valor_total', 'pago', 'data_pedido')
    list_filter = ('pago', 'entregador', 'data_pedido')
    ordering = ('-data_pedido',)
    fieldsets = (
        ('Informações do Pedido', {
            'fields': ('cliente', 'produto', 'descricao', 'observacoes')
        }),
        ('Valores (R$)', {
            'fields': ('valor_produto', 'taxa_servico', 'valor_total')
        }),
        ('Status e Pagamento', {
            'fields': ('entregador', 'forma_pagamento', 'pago')
        }),
    )
    readonly_fields = ('taxa_servico', 'valor_total',) # Campos calculados não devem ser editáveis


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Cliente)
admin.site.register(Entregadores)
admin.site.register(StatusPedido)