from django.contrib import admin
from .models import Evento
from .models import Professores
from .models import Alunos, Cursos


admin.site.register(Evento)
admin.site.register(Professores)
admin.site.register(Alunos)
admin.site.register(Cursos)
