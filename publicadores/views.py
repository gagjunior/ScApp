from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from publicadores.models import Grupo, Publicador, Atividade
from publicadores.forms import AtividadeForm


@login_required
def index(request):
    context = {
        'titulo':'Menu'
    }
    return render(request, 'index.html', context=context)


@login_required
def lista_atividades(request):        
    
    if request.method == "POST":
        form = AtividadeForm(request.POST)

        if form.is_valid():
            mes_inicio = form.cleaned_data['mes_inicio']
            ano_inicio = form.cleaned_data['ano_inicio']
            mes_fim = form.cleaned_data['mes_fim']
            ano_fim = form.cleaned_data['ano_fim']

            atividades_flt = Atividade.objects.filter(mes_relatorio__gte=mes_inicio, ano_relatorio__gte=ano_inicio, mes_relatorio__lte=mes_fim, ano_relatorio__lte=ano_fim)

            context = {
                'form':form,
                'atividades_flt':atividades_flt
            }            

    else:
        form = AtividadeForm()
        context = {'form':form}
        
    return render(request, 'publicadores/atividades_lista.html', context)

    


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



    