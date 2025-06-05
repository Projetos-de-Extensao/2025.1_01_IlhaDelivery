# app/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome


class Entregador(models.Model):
    STATUS_CHOICES = [
        ('Disponível', 'Disponível'), 
        ('Ocupado', 'Ocupado')]

    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Disponível')
    localizacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    FORMAS_PAGAMENTO_CHOICES = [
        ('Crédito', 'Crédito'),
        ('Débito', 'Débito'),
        ('Pix', 'Pix'),
        ('Dinheiro', 'Dinheiro'),
    ]

    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    entregador = models.ForeignKey("Entregador", on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(blank=True, null=True) # Mantendo como estava
    data_pedido = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True) # Pode ser usado para outras observações
    pago = models.BooleanField(default=False)
    produto = models.CharField(max_length=255, blank=True, null=True)  # Adicionado para manter compatibilidade com o HTML
    forma_pagamento = models.CharField(max_length=50,choices=FORMAS_PAGAMENTO_CHOICES,blank=True, null=True)

    def clean(self):
        if self.cliente and not self.pago: 
            if not self.pk:
                pedidos_abertos_do_cliente = Pedido.objects.filter(cliente=self.cliente, pago=False)
                if pedidos_abertos_do_cliente.exists():
                    raise ValidationError(
                        f"O cliente {self.cliente.nome} já possui um pedido em aberto. "
                        "Finalize ou pague o pedido existente antes de criar um novo."
                    )
        super().clean() 


    def save(self, *args, **kwargs):
        self.full_clean()  # Garante que as validações sejam executadas
        super().save(*args, **kwargs)

    def confirmar_pagamento(self):
        if self.pago:
            raise ValueError("O pedido já foi pago.")
        self.pago = True
        StatusPedido.objects.create(pedido=self, status='Pago')

    def confirmar_entrega(self):
        latest_status = self.status_pedido.order_by('-data_status').first()
        if not self.pago:
            raise ValueError("Pedido não pode ser entregue sem pagamento.")
        if latest_status.status != 'Em Transporte':
            raise ValueError("Pedido não está em transporte.")
        StatusPedido.objects.create(pedido=self, status='Entregue')

    def __str__(self):
        return f"Pedido #{self.id}"


# myapp/models.py
class StatusPedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Em Preparo', 'Em Preparo'), # Adicionado "Em Preparo" para corresponder ao HTML
        ('Em Transporte', 'A caminho'), # "A caminho" como no HTML
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'), # Opcional
    ]
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='status_pedido')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    data_status = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Status do Pedido #{self.pedido.id} - {self.get_status_display()}"
