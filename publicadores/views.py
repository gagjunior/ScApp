from django.shortcuts import render
from django.views import generic
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from publicadores.models import Grupo, Publicador, Atividade
from publicadores.forms import AtividadeForm, ResumoForm


@login_required
def index(request):
    context = {
        'titulo': 'Menu'
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

            atividades_flt = Atividade.objects.filter(
                mes_relatorio__gte=mes_inicio, ano_relatorio__gte=ano_inicio, mes_relatorio__lte=mes_fim, ano_relatorio__lte=ano_fim)

            context = {
                'form': form,
                'atividades_flt': atividades_flt,
                'titulo': 'Lista de Atividades'
            }

    else:
        form = AtividadeForm()
        context = {'form': form}

    return render(request, 'publicadores/atividades_lista.html', context)


@login_required
def resumo_mes_betel(request):
    if request.method == "POST":
        form = ResumoForm(request.POST)
        if form.is_valid():
            mes_inicio = form.cleaned_data['mes_inicio']
            ano_inicio = form.cleaned_data['ano_inicio']

            #Filtra o periodo
            atividades_resumo = Atividade.objects.filter(
                mes_relatorio=mes_inicio, ano_relatorio=ano_inicio)

            #--- Atividades dos Publicadores ---#           
            atv_publicadores = atividades_resumo.filter(publicador__atuacao_pub='Pb') #Filtra por publicador
            pub_qtd_relat = atv_publicadores.exclude(horas=0).count() #Total que relatou
            pub_total_public = atv_publicadores.aggregate(Sum('publicacoes')) #Total de publicações
            pub_total_videos = atv_publicadores.aggregate(Sum('videos')) #Total de videos            
            pub_total_horas = atv_publicadores.aggregate(Sum('horas')) #Total de horas
            pub_total_revis = atv_publicadores.aggregate(Sum('revisitas')) #Total de revisitas
            pub_total_estud = atv_publicadores.aggregate(Sum('estudos')) #Total de estudos

            #--- Atividades dos Pioneiros Auxiliares ---#
            atv_auxiliares = atividades_resumo.filter(publicador__atuacao_pub='Pa') #Filtra por P. Auxiliar
            aux_qtd_relat= atv_auxiliares.exclude(horas=0).count() #Total que relatou
            aux_total_public= atv_auxiliares.aggregate(Sum('publicacoes')) 
            aux_total_videos= atv_auxiliares.aggregate(Sum('videos')) #Total de videos            
            aux_total_horas= atv_auxiliares.aggregate(Sum('horas')) #Total de horas
            aux_total_revis= atv_auxiliares.aggregate(Sum('revisitas')) #Total de revisitas
            aux_total_estud= atv_auxiliares.aggregate(Sum('estudos')) #Total de estudos

            #--- Atividades dos Pioneiros Regulares ---#
            atv_regulares = atividades_resumo.filter(publicador__atuacao_pub='Pr') #Filtra por P. Regular
            reg_qtd_relat= atv_regulares.exclude(horas=0).count() #Total que relatou
            reg_total_public= atv_regulares.aggregate(Sum('publicacoes')) 
            reg_total_videos= atv_regulares.aggregate(Sum('videos')) #Total de videos            
            reg_total_horas= atv_regulares.aggregate(Sum('horas')) #Total de horas
            reg_total_revis= atv_regulares.aggregate(Sum('revisitas')) #Total de revisitas
            reg_total_estud= atv_regulares.aggregate(Sum('estudos')) #Total de estudos

            #--- Total Geral Atividades ---#      
            qtd_relat= atividades_resumo.exclude(horas=0).count()
            total_public= atividades_resumo.aggregate(Sum('publicacoes'))
            total_videos= atividades_resumo.aggregate(Sum('videos'))           
            total_horas= atividades_resumo.aggregate(Sum('horas'))
            total_revis= atividades_resumo.aggregate(Sum('revisitas'))
            total_estud= atividades_resumo.aggregate(Sum('estudos'))
            
            context = {
                'form': form,
                
                'atividades_resumo': atividades_resumo,

                'pub_qtd_relat': pub_qtd_relat,
                'aux_total_public': pub_total_public,
                'pub_total_videos': pub_total_videos,
                'pub_total_horas': pub_total_horas,
                'pub_total_revis': pub_total_revis,
                'pub_total_estud': pub_total_estud,

                'aux_qtd_relat': aux_qtd_relat,
                'aux_total_public': aux_total_public,
                'aux_total_videos': aux_total_videos,            
                'aux_total_horas': aux_total_horas, 
                'aux_total_revis': aux_total_revis,
                'aux_total_estud': aux_total_estud,

                'reg_qtd_relat': reg_qtd_relat,
                'reg_total_public': reg_total_public,
                'reg_total_videos': reg_total_videos,            
                'reg_total_horas': reg_total_horas, 
                'reg_total_revis': reg_total_revis,
                'reg_total_estud': reg_total_estud,

                'qtd_relat': qtd_relat,
                'total_public': total_public,
                'total_videos': total_videos,            
                'total_horas': total_horas, 
                'total_revis': total_revis,
                'total_estud': total_estud,

                'titulo': 'Resumo Atividades'
            }

    else:
        form = ResumoForm()
        context = {
            'form': form,
            'titulo': 'Resumo Atividades'       
        }

    return render(request, 'publicadores/resumo_mes_betel.html', context)


class GruposListView(LoginRequiredMixin, generic.ListView):
    model = Grupo

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
        context = super(PublicadoresDetailView,
                        self).get_context_data(**kwargs)
        context['titulo'] = 'Publicador'
        return context
