from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(
        max_length=11,
        unique=True,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^\d{11}$', 'O CPF deve conter 11 dígitos')]
    )

    def __str__(self):
        return self.nome

class Entregador(models.Model):
    STATUS_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Ocupado', 'Ocupado'),
    ]
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    entregador = models.ForeignKey(Entregador, on_delete=models.SET_NULL, null=True, blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.nome}"

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
    nota = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField()

    def __str__(self):
        return f"Avaliação {self.nota}/5 para {self.produto.nome}"
