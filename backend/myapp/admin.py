from django.contrib import admin
from .models import(
    Pedido,
    Cliente,    
    Entregador,
    ItemPedido,
    StatusPedido,

) 
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'entregador', 'observacoes')


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Cliente)
admin.site.register(Entregador)
admin.site.register(ItemPedido)
admin.site.register(StatusPedido)





