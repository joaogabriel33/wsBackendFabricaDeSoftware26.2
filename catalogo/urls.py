from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlataformaViewSet, GeneroViewSet, JogoViewSet, AvaliacaoViewSet, lista_jogos

router = DefaultRouter()
router.register(r'plataformas', PlataformaViewSet, basename='plataforma')
router.register(r'generos', GeneroViewSet, basename='genero')
router.register(r'jogos', JogoViewSet, basename='jogo')
router.register(r'avaliacoes', AvaliacaoViewSet, basename='avaliacao')

urlpatterns = [
    path('', include(router.urls)),
    path('pagina/jogos/', lista_jogos, name='lista_jogos'),
]