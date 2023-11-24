from django.shortcuts import render

@login_required
def pagina_index(request):
    return render(request, 'index.html')

def pagina_login(request):
    return render(request, 'login.html')
