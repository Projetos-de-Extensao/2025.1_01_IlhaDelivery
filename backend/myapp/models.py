from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)

    def confirmar_entrega_pedido(self, pedido):
        if pedido.cliente != self:
            raise ValueError("Este pedido não pertence a este cliente.")
        if not pedido.pago:
            raise ValueError("O pedido não pode ser confirmado como entregue porque ainda não foi pago.")
        if pedido.status != 'Em Transporte':
            raise ValueError("O pedido não está em transporte para ser confirmado como entregue.")
        
        pedido.atualizar_status('Entregue')

    def __str__(self):
        return self.nome


class Entregador(models.Model):
    STATUS_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Ocupado', 'Ocupado'),
    ]
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Disponível')
    localizacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Em Transporte', 'Em Transporte'),
        ('Entregue', 'Entregue'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    entregador = models.ForeignKey(Entregador, on_delete=models.SET_NULL, null=True, blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pendente')
    pago = models.BooleanField(default=False)

    def confirmar_pagamento(self):
        if self.pago:
            raise ValueError("O pedido já foi pago.")
        self.pago = True
        self.atualizar_status('Pago')

    def atualizar_status(self, novo_status):
        self.status = novo_status
        self.save()
        StatusEntrega.objects.create(pedido=self, status=novo_status)

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.nome} - Status: {self.status} - Pago: {'Sim' if self.pago else 'Não'}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (Pedido #{self.pedido.id})"


class StatusEntrega(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Transporte', 'Em Transporte'),
        ('Entregue', 'Entregue'),
    ]
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='status_entrega')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    horario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status} - Pedido #{self.pedido.id} às {self.horario.strftime('%d/%m %H:%M')}"


class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    comentario = models.TextField()
    nota = models.PositiveIntegerField() 

    def __str__(self):
        return f"Avaliação {self.nota}/5 para {self.produto.nome}"


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Carrinho de {self.cliente.nome}"


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} no carrinho de {self.carrinho.cliente.nome}"
