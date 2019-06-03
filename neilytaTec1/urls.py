"""neilytaTec1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cursodjango.views import home, listagem, listarProf
from cursodjango.views import listarAlunos, listarCursos
from cursodjango.views import update, remove, create

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('create/<int:code>/', create, name='go2create'),
    path('listagem/', listagem, name='url_listagem'),
    path('listar_prof/', listarProf, name='go2listarprof'),
    path('listar_alunos/', listarAlunos, name='go2listaralunos'),
    path('listar_cursos/', listarCursos, name='go2listarcursos'),
    path('update/<int:code>/<int:pk>/', update, name='url_update'),
    path('remove/<int:code>/<int:pk>/', remove, name='url_remove'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
