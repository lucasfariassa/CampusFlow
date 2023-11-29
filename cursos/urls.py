from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos, name="cursos"),
    path('<str:nome_curso>/<str:nome_modulo>/<str:nome_aula>/', views.aula_detail, name='aula_detail'),
]
