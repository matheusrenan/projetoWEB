from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Categoria, Produto


# Create your views here.
def home(request):
	listaCategorias = Categoria.objects.all() 
	listaProdutos = Produto.objects.all()
	template = 'home.html'
	return render(request, template, {'listaCategorias': listaCategorias, 'listaProdutos': listaProdutos})

def sobre(request):
	context = {}
	template = 'sobre.html'
	return render(request, template, context)

@login_required
def perfilUsuario(request):
	usuario = request.user
	context = {'usuario': usuario}
	template = 'perfil.html'
	return render(request, template, context)

def listaPorCategoria(request, pk):
	categoria = get_object_or_404(Categoria, pk=pk)
	listaCategorias = Categoria.objects.all()
	listaProdutos = Produto.objects.filter(categoria=categoria)
	template = 'listaPorCategoria.html'
	return render(request, template, {'listaCategorias': listaCategorias, 'listaProdutos': listaProdutos})