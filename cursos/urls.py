from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.cursos, name="cursos"),
path('<str:nome_curso>/<str:nome_modulo>/<str:nome_aula>/', views.aula_detail, name='aula_detail'),    path('curso/<int:curso_id>/', views.detalhes_curso, name='detalhes_curso'),
]
