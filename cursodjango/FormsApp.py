from django.forms import ModelForm
from .models import Professores, Alunos
from cursodjango.models import Cursos


class ProfForm(ModelForm):
    class Meta:
        model = Professores
        fields = ['nomeProf', 'formacao', 'tituloAc', 'cursoLec', 'anoInicio', 'turmas', 'membroOrg']


class AlunoForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['nomeAlu', 'ano', 'curso', 'genero', 'idade', 'ehdestaque']


class CursoForm(ModelForm):
    class Meta:
        model = Cursos
        fields = ['nomeCurso', 'dataInicio', 'numAlunos', 'numProf', 'alunosFormados', 'descricao']