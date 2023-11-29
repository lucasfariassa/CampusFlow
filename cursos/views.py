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

    context = {
        'curso': curso,
        'modulo': modulo,
        'video_aula': video_aula,
    }
    return render(request, 'visualizacao_de_aula.html', context)

@login_required(login_url="/alunos/login/")
def cursos(request):
    user = request.user
    if hasattr(user, 'aluno') and user.aluno.tipo_usuario == Aluno.USER_TIPO:
        return HttpResponseRedirect(redirect_to='/alunos/home/')
    elif hasattr(user, 'atletica') and user.atletica.tipo_usuario == Atletica.USER_TIPO:
        return HttpResponseRedirect(redirect_to='/atleticas/home/')
    else:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")