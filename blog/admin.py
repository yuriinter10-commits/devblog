from django.contrib import admin
from .models import Categoria, Artigo, MensagemContato
# Register your models here.
admin.site.register(Categoria)


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'data_publicacao')
    #===============================================================#
    search_fields = ('titulo', 'conteudo', 'autor')
    #===============================================================#
    list_filter = ('categoria', 'data_publicacao')
    
admin.site.register( MensagemContato)