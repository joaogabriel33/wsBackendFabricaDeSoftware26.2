from rest_framework import viewsets, permissions
from .models import Plataforma, Genero, Jogo, Avaliacao
from .serializers import (
    PlataformaSerializer,
    GeneroSerializer,
    JogoSerializer,
    JogoDetalheSerializer,
    AvaliacaoSerializer,
)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Jogo
from .forms import AvaliacaoForm


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

def lista_jogos(request):
    jogos = Jogo.objects.annotate(media_notas=Avg('avaliacoes__nota')).order_by('-criado_em')

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            return redirect('lista_jogos')
    else:
        form = AvaliacaoForm()

    contexto = {
        'jogos': jogos,
        'form': form,
    }
    return render(request, 'catalogo/lista_jogos.html', contexto)