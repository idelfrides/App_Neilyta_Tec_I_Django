from django.db import models

# Create your models here.

class Evento(models.Model):
    nomeEvento = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    descricao = models.TextField()

    def __str__(self):
        return  self.nomeEvento

    class Meta:
        verbose_name_plural='Evento'


class Cursos(models.Model):
    nomeCurso = models.CharField(max_length=100)
    dataInicio = models.DateField()
    numAlunos = models.IntegerField()
    numProf = models.IntegerField()
    alunosFormados = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
         return '%s' % (self.nomeCurso)

    class Meta:
        verbose_name_plural = 'Cursos'


class Professores(models.Model):
    nomeProf = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100, default='Eng. Computação')
    tituloAc = models.CharField(max_length=30)
    cursoLec = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    anoInicio = models.CharField(max_length=4)
    turmas = models.IntegerField()
    membroOrg = models.BooleanField(default=True)

    def __str__(self):
        return self.nomeProf

    class Meta:
        verbose_name_plural = 'Professores'


class Alunos(models.Model):
    nomeAlu = models.CharField(max_length=100)
    ano = models.IntegerField(default=3)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    genero = models.CharField(max_length=1, default='M')
    idade = models.IntegerField()
    ehdestaque = models.BooleanField()

    def __str__(self):
        return self.nomeAlu

    class Meta:
        verbose_name_plural = 'Alunos'