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


class GruposListView(LoginRequiredMixin, generic.ListView):
    model= Grupo

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GruposListView, self).get_context_data(**kwargs)
        context['titulo'] = 'Lista de Grupos'
        return context


class PublicadoresListView(LoginRequiredMixin, generic.ListView):
    model = Publicador

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublicadoresListView, self).get_context_data(**kwargs)
        context['titulo'] = 'Lista de Publicadores'
        return context

class PublicadoresDetailView(LoginRequiredMixin, generic.DetailView):
    model = Publicador

    def get_context_data(self, **kwargs):
        context = super(PublicadoresDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Publicador'
        return context


class AtividadesListView(LoginRequiredMixin, generic.ListView):
    model = Atividade
    