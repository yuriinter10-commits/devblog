from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Categoria
from .forms import Contatoform
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from.models import Artigo,Categoria
from. forms import Contatoform
from .serializers import ArtigoSerializer


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
    contexto ={
        'lista_categorias': categorias,
    }
    return render(request, "blog/sobre.html", contexto)

#======================================================#
def fale_conosco(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        formulario = Contatoform(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')

    else:
        formulario = Contatoform()
    
    contexto = {
        'lista_categorias': categorias,
        'form':formulario
    }
    return render(request, "blog/contato.html", contexto)
@api_view(['GET'])
def api_listar_artigos(request):
    # 1. Obter todos os artigos do banco de dados
    artigos = Artigo.objects.all()
    # 2. Jogamos os artigos na "Máquina" (many=True porque é uma lista!) 
    serializer = ArtigoSerializer(artigos, many=True)
    # 3. Devolvemos os dados serializados em formato JSON
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_criar_artigo(request):
    serializer = ArtigoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)