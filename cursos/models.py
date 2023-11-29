from django.db import models
from utils.cursos_academicos import OPCOES_CURSOS


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_lancamento = models.DateField(auto_now_add=True)
    curso_academico_relacionado = models.CharField(max_length=3)
    thumbnail = models.ImageField(upload_to='static/images/thumbs_cursos', default='static/images/global/thumb_curso_default.png')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
class Modulo(models.Model):
    curso = models.ForeignKey(Curso, related_name='modulos', on_delete=models.CASCADE)
    titulo_modulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo_modulo
    
    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
    
class Videoaula(models.Model):
    modulo = models.ForeignKey(Modulo, related_name='videoaulas', on_delete=models.CASCADE)
    titulo_video = models.CharField(max_length=100)
    data_publicacao = models.DateField(auto_now_add=True)
    descricao_video = models.TextField(max_length=300)
    url_video = models.URLField()

    def __str__(self):
        return self.titulo_video
    
    @property
    def nome_curso(self):
        return self.modulo.curso.nome
    
    class Meta:
        verbose_name = 'Videoaula'
        verbose_name_plural = 'Videoaulas'
