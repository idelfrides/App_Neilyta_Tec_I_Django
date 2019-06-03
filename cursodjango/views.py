from django.shortcuts import render, redirect
from .models import Professores, Alunos, Cursos
from .FormsApp import ProfForm, AlunoForm, CursoForm


from .models import Evento

# Create your views here.


def home(request):
    # dados = {}
    # dados_evento = {}
    # dados_prof = {}
    # dados_alunos = {}
    # dados_cursos = {}
    # dados['inicio'] = a pagina home da aplicação'

    # dados= {'chave': 'valor'}
    # evento = evento
    dados_evento = {'title': 'Minicurso Django 2.2.1'}
    dados_evento['title_secao_ev'] = 'evento'
    dados_evento['evento'] = Evento.objects.all()

    # dados_prof['title_secao_real'] = 'realização'
    # dados_prof['membros'] = Professores.objects.filter(membroOrg=True)

    # dados_alunos['title_secao_dest'] = 'alunos destaque'
    # dados_alunos = Alunos.objects.filter(ehdestaque=True)

    # dados_cursos['title_secao_cur'] = 'cursos'
    # dados_cursos = Cursos.objects.all()

    # dados['dados_geral'] = dict(dados_evento, **dados_prof)

    return render(request, 'cursodjango/home.html', dados_evento)


def listagem(request):
    dados = {'info':'Listagem de professores, alunis, cursos, membrosa da diretoria'}
    return render(request, 'cursodjango/listagem.html', dados)


# CRUD -> CREATE | READ | UPDATE | DELETE

# -------------------------------------
#1            CREATE
# -------------------------------------
def create(request, code):
    if code == 1:  # create professor
        dados = {}
        dados['acao'] = 'Cadastro de Professores'
        dados['info'] = 'Cadastro de um(a) novo(a) Prof(ra). '
        form = ProfForm(request.POST or None)
        dados['form'] = form

        if form.is_valid():
            form.save()
            return redirect('go2listarprof')

        return render(request, 'cursodjango/cadastro.html', dados)

    elif code == 2: # create aluno
        dados = {}
        dados['acao'] = 'Cadastro de Alunos'
        dados['info'] = 'Cadastro de um(a) novo(a) Aluno(a)'
        form = AlunoForm(request.POST or None)
        dados['form'] = form

        if form.is_valid():
            form.save()
            return redirect('go2listaralunos')

        return render(request, 'cursodjango/cadastro.html', dados)

    elif code == 3:  # create curso
        dados = {}
        dados['acao'] = 'Cadastro de Cursos'
        dados['info'] = 'Cadastro de um novo Curso '
        form = CursoForm(request.POST or None)
        dados['form'] = form

        if form.is_valid():
            form.save()
            return redirect('go2listarcursos')

        return render(request, 'cursodjango/cadastro.html', dados)
    else:
        return redirect('url_listagem')


# -------------------------------------
# 2            READ
# -------------------------------------
def listarProf(request):
    dadosProf = {}
    dadosProf['info'] = 'Listagem de professores com  algumas de suas respectivas informações'
    dadosProf['professores'] = Professores.objects.all()
    return render(request, 'cursodjango/listarProf.html', dadosProf)


def listarAlunos(request):
    dadosAlunos = {}
    dadosAlunos['info'] = 'Listagem de alunos com  algumas de suas respectivas informações'
    dadosAlunos['alunos'] = Alunos.objects.all()
    return render(request, 'cursodjango/listarAlunos.html', dadosAlunos)


def listarCursos(request):
    dadosCursos = {}
    dadosCursos['cursos'] = Cursos.objects.all()
    return render(request, 'cursodjango/listarCuros.html', dadosCursos)

# -------------------------------------
# 3            UPDATE
# -------------------------------------
def update(request, code, pk):
    if code == 1:  # update professor
        dados = {}
        dados['info'] = 'Atualização de dados do Prof. '
        profData = Professores.objects.get(id = pk)
        form = ProfForm(request.POST or None, instance=profData)

        if form.is_valid():
            form.save()
            return redirect('go2listarprof')

        dados['update_prof'] = profData
        dados['form'] = form
        return render(request, 'cursodjango/formUpdateProf.html', dados)

    elif code == 2: # update aluno
        dados = {}
        dados['info'] = 'Atualização de dados do(a) aluno(a) '
        alunoData = Alunos.objects.get(id = pk)
        dados['update_aluno'] = alunoData

        form = AlunoForm(request.POST or None, instance=alunoData)

        if form.is_valid():
            form.save()
            return redirect('go2listaralunos')

        dados['form'] = form
        return render(request, 'cursodjango/formUpdateAluno.html', dados)

    elif code == 3:  # update curso
        dados = {}
        dados['info'] = 'Atualização de dados do Curso '
        cursoData = Cursos.objects.get(id = pk)
        form = CursoForm(request.POST or None, instance=cursoData)

        if form.is_valid():
            form.save()
            return redirect('go2listarcursos')

        dados['update_curso'] = cursoData
        dados['form'] = form
        return render(request, 'cursodjango/formUpdateCurso.html', dados)
    else:
        return redirect('url_listagem')


# -------------------------------------
# 4            DELETE
# -------------------------------------
def remove(request, code, pk):
    if code == 1:  # remove professor
        profData = Professores.objects.get(id = pk)
        profData.delete()
        return redirect('go2listarprof')

    elif code == 2: # remove aluno
        alunoData = Alunos.objects.get(id = pk)
        alunoData.delete()
        return redirect('go2listaralunos')

    elif code == 3:  # remove curso
        cursoData = Cursos.objects.get(id = pk)
        cursoData.delete()
        return redirect('go2listarcursos')
    else:
        return redirect('url_listagem')


