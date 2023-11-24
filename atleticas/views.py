from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/atleticas/login/")
def home_atleticas(request):
    return render(request, 'home_atleticas.html')

def login_atleticas(request):
    return render(request, 'login_atleticas.html')
