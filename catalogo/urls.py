from rest_framework.routers import DefaultRouter
from .views import PlataformaViewSet, GeneroViewSet, JogoViewSet, AvaliacaoViewSet

router = DefaultRouter()
router.register(r'plataformas', PlataformaViewSet, basename='plataforma')
router.register(r'generos', GeneroViewSet, basename='genero')
router.register(r'jogos', JogoViewSet, basename='jogo')
router.register(r'avaliacoes', AvaliacaoViewSet, basename='avaliacao')

urlpatterns = router.urls