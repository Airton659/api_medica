from django.contrib import admin
from .models import Profissional

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'nome_social', 'profissao', 'endereco', 'contato')
