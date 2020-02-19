from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from publicadores.models import Grupo, Publicador, Atividade


@login_required
def index(request):
    context = {
        'titulo':'Menu'
    }
    return render(request, 'index.html', context=context)



class PublicadoresListView(LoginRequiredMixin, generic.ListView):
    model = Publicador
    titulo = 'Lista Publicadores'