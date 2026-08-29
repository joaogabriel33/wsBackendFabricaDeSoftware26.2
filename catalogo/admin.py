from django.contrib import admin
from .models import Plataforma, Genero, Jogo, Avaliacao


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criado_em')
    search_fields = ('nome',)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criado_em')
    search_fields = ('nome',)


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_lancamento', 'criado_em')
    search_fields = ('titulo',)
    filter_horizontal = ('plataformas', 'generos')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'jogo', 'usuario', 'nota', 'criado_em')
    list_filter = ('nota',)