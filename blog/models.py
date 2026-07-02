from django.db import models

# blog/models.py
class Categoria(models.Model):
    # Coluna de texto curto (máximo 100 caracteres)
    nome = models.CharField(max_length=100)

    # Como o objeto deve ser lido por humanos no painel
    def __str__(self):
        return self.nome

# 2. Tabela de Artigos
class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    # Texto longo, sem limite de caracteres
    conteudo = models.TextField()
    # Preenche com a data/hora exata do cadastro
    data_publicacao = models.DateTimeField(auto_now_add=True)

    # Relação com a Categoria (ForeignKey = Chave Estrangeira)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    autor = models.CharField(max_length=100, default="Admin")

    def __str__(self):
        return self.titulo
