from django.db import models


GENDER_CHOICE = [
    ('MASCULINO', 'Masculino'),
    ('FEMININO', 'Feminino'),
]

PROF_TITLE_CHOICE = [
    ('BACHAREL', 'Bacharel'),
    ('ESPECIALISATA', 'Especialista'),
    ('MESTRE', 'Mestre'),
    ('PHD', 'PhD'),
]

COURSES_CHOICE = [
    ('TÉCNICO EM INFORMÁTICA', 'TÉCNICO EM INFORMÁTICA'),
    ('TÉCNICO EM AGROPECUÁRIA', 'TÉCNICO EM EM AGROPECUÁRIA'),
    ('TÉCNICO EM ELETROMECÂNICA', 'TÉCNICO EM ELETROMECÂNICA'),
    ('TÉCNICO EM FINANÇAS', 'TÉCNICO EM FINANÇAS'),
]


class Evento(models.Model):
    nome_Evento = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    descricao = models.TextField()

    def __str__(self):
        return  self.nome_Evento

    class Meta:
        verbose_name_plural='Evento'


class Cursos(models.Model):
    nome_Curso = models.CharField(
        max_length=30, 
        choices=COURSES_CHOICE
    )
    data_Inicio = models.DateField()
    num_Alunos = models.IntegerField()
    num_Prof = models.IntegerField()
    alunos_Formados = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return '%s' % (self.nome_Curso)
        

    class Meta:
        verbose_name_plural = 'Cursos'


class Professores(models.Model):
    nome_Prof = models.CharField(max_length=100)
    formacao = models.CharField(
        max_length=100, 
        default='Eng. Computação'
    )
    titulo_Academico = models.CharField(
        max_length=30, 
        choices=PROF_TITLE_CHOICE
    )
    curso_Leciona = models.ForeignKey(
        Cursos, 
        on_delete=models.CASCADE
    )
    ano_Inicio = models.CharField(max_length=4)
    turmas = models.IntegerField()
    membro_Organizacao = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_Prof

    class Meta:
        verbose_name_plural = 'Professores'


class Alunos(models.Model):
    nome_aluno = models.CharField(max_length=100)
    ano = models.IntegerField(default=3)
    curso = models.ForeignKey(
        Cursos, 
        on_delete=models.CASCADE
    )
    genero = models.CharField(
        max_length=30,
        choices=GENDER_CHOICE,
    )
    idade = models.IntegerField()
    eh_destaque = models.BooleanField()

    def __str__(self):
        return self.nome_aluno

    class Meta:
        verbose_name_plural = 'Alunos'