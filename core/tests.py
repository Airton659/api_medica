from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Profissional, Consulta
from datetime import datetime
from django.utils import timezone


class ConsultaTests(APITestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome_completo = "Teste",
            nome_social = "T",
            profissao="Teste",
            endereco= "Rua dos Testes,123",
            contato="(31) 99999-9999"
        )

    def test_criar_consulta(self):
        """
        Teste para verificar se é possível criar uma nova consulta.
        """
        url = reverse('consulta-list')
        data = {
            'data': timezone.now().isoformat(),
            'profissional': self.profissional.nome_completo
        }

        response = self.client.post(url,data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Consulta.objects.count(), 1)
        self.assertEqual(Consulta.objects.get().profissional.nome_completo, "Teste")