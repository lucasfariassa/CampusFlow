from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    USER_TIPO = 'ALU'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    matricula = models.CharField(max_length=9, primary_key=True, verbose_name='Matrícula') # Matrícula do Aluno que serve de ID para o sistema
    nome_completo = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.EmailField(max_length=254, verbose_name='Endereço de Email')
    curso_academico = models.CharField(max_length=3, verbose_name='Curso Acadêmico')
    status_monitor = models.BooleanField(default=False, verbose_name='Status de Monitor') # Status personalizável apenas pelas Atléticas
    tipo_usuario = models.CharField(max_length=3, default=USER_TIPO)
    
    class Meta:
        verbose_name = 'Aluno(a)'
        verbose_name_plural = 'Alunos'
