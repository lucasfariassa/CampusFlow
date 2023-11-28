from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from .models import Atletica

@login_required(login_url="/atleticas/login/")
def home_atleticas(request):
    user = request.user
    if hasattr(user, 'atletica') and user.atletica.tipo_usuario == Atletica.USER_TIPO:
        return render(request, 'home_atleticas.html')
    else:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

def login_atleticas(request):
    if request.method == "GET":
        return render(request, 'login_atleticas.html')
    else:
        user = request.POST.get('user_atletica')
        password = request.POST.get('senha_atletica')
        
        user_is_registered = authenticate(username=user, password=password)

        if user_is_registered:
            login_django(request, user_is_registered)
            return HttpResponseRedirect(redirect_to='/atleticas/home/')
        else:
            return HttpResponse('Seu usuário e/ou senha podem estar errados!') # MODIFICAR

@login_required(login_url="/atleticas/login/")
def cadastrar_monitor(request):
    user = request.user
    if hasattr(user, 'atletica') and user.atletica.tipo_usuario == Atletica.USER_TIPO:
        return render(request, 'cadastro_de_monitor.html')
    else:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

@login_required(login_url="/atleticas/login/")
def visualizar_cursos(request):
    user = request.user
    if hasattr(user, 'atletica') and user.atletica.tipo_usuario == Atletica.USER_TIPO:
        return render(request, 'visualizacao_de_cursos.html')
    else:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

@login_required(login_url="/atleticas/login/")
def criar_curso(request):
    user = request.user
    if hasattr(user, 'atletica') and user.atletica.tipo_usuario == Atletica.USER_TIPO:
        return render(request, 'criacao_de_curso.html')
    else:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")