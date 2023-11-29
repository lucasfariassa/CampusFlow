from django.contrib import admin
from .models import Curso, Modulo, Videoaula

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_lancamento', 'curso_academico_relacionado')

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('titulo_modulo', 'curso')

class VideoaulaAdmin(admin.ModelAdmin):
    list_display = ('titulo_video', 'modulo', 'nome_curso', 'data_publicacao', 'url_video')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Modulo, ModuloAdmin)
admin.site.register(Videoaula, VideoaulaAdmin)
