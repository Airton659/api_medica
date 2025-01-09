from rest_framework import viewsets
from rest_framework import permissions
from .models import Profissional, Consulta
from .serializers import ProfissionalSerializer, ConsultaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    
    @action(detail=False, methods=['get'])
    def by_profissional(self, request):
        profissional_id = request.query_params.get('profissional_id', None)
        if profissional_id is not None:
            consultas = Consulta.objects.filter(profissional_id=profissional_id)
            serializer = ConsultaSerializer(consultas, many=True)
            return Response(serializer.data)
        return Response({"detail": "Profissional ID não fornecido"}, status=400)
