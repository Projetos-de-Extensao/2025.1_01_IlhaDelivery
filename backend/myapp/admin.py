from django.contrib import admin
from .models import Produto, Pedido, Avaliacao, Cliente

admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Avaliacao)
admin.site.register(Cliente)
