from django.db import models
import django.db.models.deletion

# Create your models here.
class loja(models.Model):
	nome = models.CharField(max_length=120)
	descricao = models.TextField(default='texto default')
	def __str__(self):
		return self.nome

class Categoria(models.Model):
	id = models.BigAutoField(primary_key=True)
	nomeCategoria = models.CharField(max_length=120)
	descricaoCategoria = models.TextField(default='texto default')

	def __str__(self):
		return self.nomeCategoria

class Produto(models.Model):
	id = models.BigAutoField(primary_key=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	nomeProduto = models.CharField(max_length=120)
	descricaoProduto = models.TextField(default='texto default')
	imagemProduto = models.FileField(upload_to= 'images/', blank=True)
	precoProduto = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.nomeProduto