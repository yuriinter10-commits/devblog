from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Categoria
from .forms import Contatoform


def home(request):
    
    categorias = Categoria.objects.all()
    
    noticias = Artigo.objects.all()
    
    contexto ={
        'lista_artigos': noticias,
        'lista_categorias': categorias,
    }
    
    return render(request, "blog/index.html", contexto)
#======================================================#
def sobre_nos(request):
    categorias = Categoria.objects.all()
    return render(request, "blog/sobre.html")
#======================================================#
def fale_conosco(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        formulario = Contatoform
        (request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')

    else:
        formulario = Contatoform()
    
    contexto = {
        'lista_categorias': categorias,
        'lista_categorias': categorias,
        'form':formulario
    }
    return render(request, "blog/contato.html", contexto)