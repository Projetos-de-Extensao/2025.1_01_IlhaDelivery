from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
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
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    loja = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido de {self.quantidade} de {self.produto.nome}"

class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    nota = models.PositiveIntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"Avaliação de {self.nota} para {self.produto.nome} por {self.usuario}"


