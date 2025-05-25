# app/models.py
from django.db import models
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
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    entregador = models.ForeignKey("Entregador", on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(default="Sem descrição")
    data_pedido = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)
    pago = models.BooleanField(default=False)

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

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
    
class StatusPedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Em Transporte', 'Em Transporte'),
        ('Entregue', 'Entregue'),
    ]
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='status_pedido')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    data_status = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Status do Pedido #{self.pedido.id} - {self.status}"

