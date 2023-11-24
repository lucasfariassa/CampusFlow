from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome_completo', 'email', 'curso_academico', 'status_monitor')
admin.site.register(Aluno)
