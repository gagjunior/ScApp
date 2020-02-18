from django.shortcuts import render
from django.views import generic
from publicadores.models import Grupo, Publicador, Atividade

def index(request):
    context = {
        'titulo':'Menu'
    }
    return render(request, 'index.html', context=context)



class PublicadoresListView(generic.ListView):
    model = Publicador
    titulo = 'Lista Publicadores'