from django.db import models
from django.contrib.auth.models import User
from utils.cursos_academicos import OPCOES_CURSOS

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=9, primary_key=True) # Matrícula do Aluno que serve de ID para o sistema
    nome_completo = models.CharField(max_length=100)
    curso_academico = models.CharField(max_length=3)
    status_monitor = models.BooleanField(default=False) # Status personalizável apenas pelas Atléticas

    class Meta:
        verbose_name = 'Aluno(a)'
        verbose_name_plural = 'Alunos'
