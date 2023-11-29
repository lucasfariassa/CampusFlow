from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_atleticas, name='login_atleticas'),
    path('home/', views.home_atleticas, name='home_atleticas'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrar-monitor/', views.cadastrar_monitor, name='cadastrar_monitor'),
    path('cursos/', views.visualizar_cursos, name='visualizar_cursos'),
    path('criar-curso/', views.criar_curso, name='criar_curso'),
]
