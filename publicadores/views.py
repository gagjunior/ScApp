# Importações Django
from django.shortcuts import render
from django.views import generic
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Importações pacote Publicadores
from publicadores import LISTA_MES, data_atual, num_seis_meses, ano_seis_meses
from publicadores.models import Grupo, Publicador, Atividade
from publicadores.forms import AtividadeForm, ResumoForm, NaoRelatouForm


@login_required
def index(request):
    context = {
        'titulo': 'Menu'
    }
    return render(request, 'index.html', context)


@login_required
def lista_atividades(request):
    titulo = 'Lista de Atividades'
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
                'titulo': titulo
            }

    else:
        form = AtividadeForm()
        context = {
            'form': form,
            'titulo': titulo
        }

    return render(request, 'publicadores/atividades_lista.html', context)


@login_required
def resumo_mes_betel(request):
    titulo = 'Resumo de Atividades'
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

            mensagem_titulo = 'Aviso!'
            mensagem_corpo1 = 'Não houve informações a listar para o periodo solicitado.'
            mensagem_corpo2 = 'Favor verificar os critérios de pesquisa.'
            
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

                'mensagem_titulo': mensagem_titulo,
                'mensagem_corpo1': mensagem_corpo1,
                'mensagem_corpo2': mensagem_corpo2,

                'titulo': titulo
            }

    else:
        form = ResumoForm()

        mensagem_titulo = 'Resumo para Betel'
        mensagem_corpo1 = 'Para visualizar as informações selecione o ano e o mês desejado.'
        mensagem_corpo2 = 'Essas informações devem ser enviadas para Betel até no máximo dia 20 do mês subsequente.'

        context = {
            'form': form,
            'mensagem_titulo': mensagem_titulo,
            'mensagem_corpo1': mensagem_corpo1,
            'mensagem_corpo2': mensagem_corpo2,
            
            'titulo': titulo
        }

    return render(request, 'publicadores/resumo_mes_betel.html', context)


@login_required
def lista_nao_relatou(request):
    titulo = 'Lista de Irregulares'
    if request.method == 'POST':
        form = NaoRelatouForm(request.POST)
        if form.is_valid():
            mes_inicio = form.cleaned_data['mes_inicio']
            ano_inicio = form.cleaned_data['ano_inicio']

            nao_relatou = Publicador.objects.exclude(
                atividade__in=Atividade.objects.filter(mes_relatorio=mes_inicio, ano_relatorio=ano_inicio)
            )

            dicionario_mes = dict(LISTA_MES)
            desc_mes = dicionario_mes[int(mes_inicio)]

            context = {
                'form': form,
                'nao_relatou': nao_relatou,
                'desc_mes': desc_mes,
                'titulo': titulo
            }
    else:
        form = NaoRelatouForm()
        context = {
            'form': form,
            'titulo': titulo
        }

    return render(request, 'publicadores/nao_relatou.html', context)


@login_required
def lista_inativos(request):
    titulo = 'Lista de Inativos'

    dicionario_mes = dict(LISTA_MES)
    desc_mes = dicionario_mes[int(num_seis_meses)]

    inativos = Publicador.objects.exclude(
                atividade__in= Atividade.objects.filter(mes_relatorio__gte=num_seis_meses, ano_relatorio=ano_seis_meses)
            )
    
    context = {
        'mes': desc_mes,
        'ano': ano_seis_meses,
        'inativos': inativos,
        'titulo': titulo
    }
    
    return render(request, 'publicadores/lista_inativos.html', context)


class GruposListView(LoginRequiredMixin, generic.ListView):
    model = Grupo
    titulo = 'Lista de Grupos'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GruposListView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context


class PublicadoresListView(LoginRequiredMixin, generic.ListView):
    model = Publicador
    titulo = 'Lista de Publicadores'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublicadoresListView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context


class PublicadoresDetailView(LoginRequiredMixin, generic.DetailView):
    model = Publicador
    titulo = 'Publicador'
    def get_context_data(self, **kwargs):
        context = super(PublicadoresDetailView,
                        self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context
