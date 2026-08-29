from rest_framework import serializers
from .models import Plataforma, Genero, Jogo, Avaliacao


class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ['id', 'nome', 'criado_em']


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome', 'criado_em']


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ['id', 'titulo', 'descricao', 'data_lancamento', 'plataformas', 'generos', 'criado_em']


class JogoDetalheSerializer(serializers.ModelSerializer):
    plataformas = PlataformaSerializer(many=True, read_only=True)
    generos = GeneroSerializer(many=True, read_only=True)

    class Meta:
        model = Jogo
        fields = ['id', 'titulo', 'descricao', 'data_lancamento', 'plataformas', 'generos', 'criado_em']


class AvaliacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Avaliacao
        fields = ['id', 'jogo', 'usuario', 'nota', 'comentario', 'criado_em']

    def validate_nota(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('A nota deve estar entre 1 e 5.')
        return value