from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from cursos.models import Curso
from .models import Aluno
from utils.cursos_academicos import OPCOES_CURSOS


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        enrollment = request.POST.get('matricula')
        password = request.POST.get('senha')
        
        user_is_registered = authenticate(username=enrollment, password=password)

        if user_is_registered:
            login_django(request, user_is_registered)
            return HttpResponseRedirect(redirect_to='/alunos/home/')
        else:
            return HttpResponse('Sua matrícula e/ou senha podem estar erradas! Ou talvez você ainda não possua um cadastro') # MODIFICAR


def cadastro(request):
    if request.method == "GET":
        context = {
            'OPCOES_CURSOS': OPCOES_CURSOS,
        }
        return render(request, 'cadastro.html', context)
    else:
        name = request.POST.get('nome_completo')
        enrollment = request.POST.get('matricula')
        password = request.POST.get('senha')
        email = request.POST.get('email')
        course_of_study = request.POST.get('curso_academico')

        user_already_exists = User.objects.filter(username=enrollment).first()

        if user_already_exists:
            return HttpResponse('Já existe um usuário com essa matrícula') # MODIFICAR
        else:
            user = User.objects.create_user(username=enrollment, password=password, email=email)
            student = Aluno.objects.create(user=user, nome_completo=name, matricula=enrollment, email=email, curso_academico=course_of_study)
            student.save()
            user_registered = authenticate(username=enrollment, password=password)
            login_django(request, user_registered) # Realiza um login automático após o cadastro - Performs an automatic login after registration
            return HttpResponseRedirect(redirect_to='/alunos/home/')

@login_required(login_url="/alunos/login/")
def home(request):
    user = request.user
    if hasattr(user, 'aluno') and user.aluno.tipo_usuario == Aluno.USER_TIPO:
        cursos = Curso.objects.all()
        context = {
            'cursos': cursos
        }
        return render(request, 'home.html', context)
    else:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
