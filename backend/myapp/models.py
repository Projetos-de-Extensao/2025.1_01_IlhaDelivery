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
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Em Transporte', 'Em Transporte'),
        ('Entregue', 'Entregue'),
    ]
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    entregador = models.ForeignKey("Entregador", on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(default="Sem descrição")
    data_pedido = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pendente')
    pago = models.BooleanField(default=False)

    def confirmar_pagamento(self):
        if self.pago:
            raise ValueError("O pedido já foi pago.")
        self.pago = True
        self.status = 'Pago'
        self.save()

    def confirmar_entrega(self):
        if not self.pago:
            raise ValueError("Pedido não pode ser entregue sem pagamento.")
        if self.status != 'Em Transporte':
            raise ValueError("Pedido não está em transporte.")
        self.status = 'Entregue'
        self.save()

    def __str__(self):
        return f"Pedido #{self.id} - {self.status}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"

