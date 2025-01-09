from rest_framework import serializers
from .models import Profissional, Consulta

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'


class ConsultaSerializer(serializers.ModelSerializer):
    profissional = serializers.SlugRelatedField(queryset=Profissional.objects.all(), slug_field='nome_completo' )

    class Meta:
        model = Consulta
        fields = [ 'data', 'profissional']