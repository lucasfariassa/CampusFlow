from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


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
            return HttpResponse('Sua matrícula e/ou senha podem estar erradas! Ou talvez você ainda não possua um cadastro')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        enrollment = request.POST.get('matricula')
        password = request.POST.get('senha')

        user_already_exists = User.objects.filter(username=enrollment).first()

        if user_already_exists:
            return HttpResponse('Já existe um usuário com essa matrícula')
        else:
            user = User.objects.create_user(username=enrollment, password=password)
            user.save()
            user_registered = authenticate(username=enrollment, password=password)
            login_django(request, user_registered) # Realiza um login automático após o cadastro - Performs an automatic login after registration
            return HttpResponseRedirect(redirect_to='/alunos/home/')


@login_required(login_url="/alunos/login/")
def home(request):
    return render(request, 'home.html')
