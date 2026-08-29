from rest_framework import viewsets, permissions
from .models import Plataforma, Genero, Jogo, Avaliacao
from .serializers import (
    PlataformaSerializer,
    GeneroSerializer,
    JogoSerializer,
    JogoDetalheSerializer,
    AvaliacaoSerializer,
)


class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return JogoDetalheSerializer
        return JogoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)