from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def pagina_index(request):
    return render(request, 'index.html')

def pagina_login(request):
    return render(request, 'login.html')
