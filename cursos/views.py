from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .models import Curso, Modulo, Videoaula
from alunos.models import Aluno
from atleticas.models import Atletica

@login_required(login_url="/alunos/login/")
def aula_detail(request, nome_curso, nome_modulo, nome_aula):
    curso = get_object_or_404(Curso, nome=nome_curso)
    modulo = get_object_or_404(Modulo, curso=curso, titulo_modulo=nome_modulo)
    video_aula = get_object_or_404(Videoaula, modulo=modulo, titulo_video=nome_aula)
    
    modulos_curso = Modulo.objects.filter(curso=curso)

    context = {
        'curso': curso,
        'modulo': modulo,
        'video_aula': video_aula,
        'modulos_curso': modulos_curso,
    }
    return render(request, 'visualizacao_de_aula.html', context)

@login_required(login_url="/alunos/login/")
def cursos(request):
    user = request.user
    if hasattr(user, 'aluno') and user.aluno.tipo_usuario == Aluno.USER_TIPO:
        return HttpResponseRedirect(redirect_to='/alunos/home/')
    elif hasattr(user, 'atletica') and user.atletica.tipo_usuario == Atletica.USER_TIPO:
        return HttpResponseRedirect(redirect_to='/atleticas/home/')

@login_required(login_url="/alunos/login/")
def sua_view(request):
    # Supondo que você tenha um módulo específico identificado
    modulo_especifico = Modulo.objects.get(nome='SeuNomeDeModulo')

    # Buscar todas as videoaulas relacionadas ao módulo específico
    videoaulas_do_modulo = Videoaula.objects.filter(modulo=modulo_especifico)

    return render(request, 'seu_template.html', {'videoaulas': videoaulas_do_modulo})

@login_required(login_url="/alunos/login/")
def detalhes_curso(request, curso_id):
    # Lógica para recuperar informações do curso com o ID fornecido
    curso = Curso.objects.get(pk=curso_id)

    # Renderizar um template com as informações do curso
    return render(request, 'detalhes_curso.html', {'curso': curso})

@login_required(login_url="/alunos/login/")
def cadastro_monitor(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'cadastro_monitor.html', context)

